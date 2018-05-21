import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
from joblib import Parallel
from joblib import delayed
from sklearn.utils import resample
from sklearn.utils.validation import check_is_fitted
from sklearn.base import BaseEstimator, clone
import warnings


class _ConstantPredictor(BaseEstimator):

    def fit(self, X, y):
        self.y_ = y
        return self

    def predict(self, X):
        check_is_fitted(self, 'y_')

        return np.repeat(self.y_, X.shape[0])

    def decision_function(self, X):
        check_is_fitted(self, 'y_')

        return np.repeat(self.y_, X.shape[0])

    def predict_proba(self, X):
        check_is_fitted(self, 'y_')

        return np.repeat([np.hstack([1 - self.y_, self.y_])],
                         X.shape[0], axis=0)

def _fit_binary(estimator, X, y, classes=None):
    """Fit a single binary estimator."""
    unique_y = np.unique(y)
    if len(unique_y) == 1:
        if classes is not None:
            if y[0] == -1:
                c = 0
            else:
                c = y[0]
            warnings.warn("Label %s is present in all training examples." %
                          str(classes[c]))
        estimator = _ConstantPredictor().fit(X, unique_y)
    else:
        estimator = clone(estimator)
        estimator.fit(X, y)
    return estimator

class OneVsRestClassifierBalance(OneVsRestClassifier):
    
    def fit(self, X, y):
        self.label_binarizer_ = LabelBinarizer(sparse_output=True)
        Y = self.label_binarizer_.fit_transform(y)
        Y = Y.tocsc()
        self.classes_ = self.label_binarizer_.classes_
        totalIns = Y.shape[0]
        XBal = []
        YBal = []
        for i in range(len(self.label_binarizer_.classes_)):
            if len(y.shape)>1:
                # Matrix
                curIdxs = Y[:,i].nonzero()[0]
            else:
                curIdxs = Y.nonzero()[0]
            baseX = X[curIdxs,:]
            if len(y.shape)>1:
                # Matrix
                baseY = y[curIdxs,:]
            else:
                # array, e.g. due to testing classifier performance for single label prediction
                baseY = y[curIdxs]
            tempX = X
            tempY = y
            imbalancedIns = baseX.shape[0]
            numDup = totalIns/imbalancedIns - 1
            for j in range(int(numDup)):
                tempX = np.vstack((tempX,baseX))
                if len(y.shape)>1:
                    tempY = np.vstack((tempY,baseY))
                else:
                    tempY = np.concatenate((tempY, baseY))
            numAdd = totalIns%imbalancedIns
            tempX = np.vstack((tempX,resample(baseX,n_samples=numAdd,random_state=0)))
            if len(y.shape)>1:
                tempY = np.vstack((tempY,resample(baseY,n_samples=numAdd,random_state=0)))
            else:
                tempY = np.concatenate((tempY,resample(baseY,n_samples=numAdd,random_state=0)))
            XBal.append(tempX)
            if len(y.shape)>1:
                YBal.append(tempY[:,i])
            else:
                YBal.append(tempY)
        self.estimators_ = Parallel(n_jobs=self.n_jobs)(delayed(_fit_binary)(
            self.estimator, XBal[i], YBal[i], classes=[
                "not %s" % self.label_binarizer_.classes_[i],
                self.label_binarizer_.classes_[i]])
            for i in range(len(YBal)))
            #for i, column in enumerate(columns))
        return self