import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
from joblib import Parallel
from joblib import delayed
from sklearn.utils import resample
from sklearn.utils.validation import check_is_fitted
from sklearn.base import BaseEstimator, clone
import warnings
from imblearn.over_sampling import SMOTE 

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

class OneVsRestClassifierSMOTE(OneVsRestClassifier):
    
    def fit(self, X, y):
        self.label_binarizer_ = LabelBinarizer(sparse_output=True)
        Y = self.label_binarizer_.fit_transform(y)
        Y = Y.tocsc()
        self.classes_ = self.label_binarizer_.classes_
        XBal = []
        YBal = []
        sm = SMOTE(random_state=42)
        for i in range(len(self.label_binarizer_.classes_)):
            Xout, Yout = sm.fit_sample(X, y[:,i])
            XBal.append(Xout)
            YBal.append(Yout)
        self.estimators_ = Parallel(n_jobs=self.n_jobs)(delayed(_fit_binary)(
            self.estimator, XBal[i], YBal[i], classes=[
                "not %s" % self.label_binarizer_.classes_[i],
                self.label_binarizer_.classes_[i]])
            for i in range(len(YBal)))
            #for i, column in enumerate(columns))
        return self