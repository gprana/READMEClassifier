# Learning-Analytics-Project

## Description of the dataset:
The dataset we will be working on is a set of events related to a programming MOOC (massive open online course). Users are asked to submit their solution to a programming assignment which are automatically graded. For each user we have at our disposal a number of informations:
* the grade of the related submission
* a timestamp of the submission
* the time between two submissions
* some events associated to a submission (e.g. if the user has watched a video, posted a message on the forum etc.) that illustrate the strategy followed by the user.


## Overall Goal:
* Explore assignment strategies
* Predict if the grade would improve after a resubmission to an assignment
* Predict grade improvement between the first and last submission to an assignment 

## Data Analysis Pipeline:
* Develop an Hypothesis
* Extract features
* Partition data into train and test set
* Train model (on train set)
* Evaluate model performance (on test set)
* Find the best feature set and model

## Hypotheses & Features Selection:
The MOOC is composed of 3 main components: videos, forum and problems. Each of these components have events associated with.
For example for the video components, we can track if a user has played a video, how long he watched it or if he paused the video. Similarly for the forum we can know if a user has posted comments, watched a thread etc.
 
 The goal here is to make relevant hypotheses and extract associated features that reflect a learning behaviour. Three features were already extracted in the Python code supplied: the duration of a video activity, the average time difference between two videos watched and the number of forum threads viewed.
 
__Hypotheses related to video events__
* the time spent watching videos has a positive effect on the next submission grade
 * --> count the time spent (`DurationOfVideoActivity`)
* the more frequently a user watches a video, the more chances he has to increase his grade
 * --> extract the duration between two videos watched and compute the mean (`AverageVideoTimeDiffs`)
* the number of different videos watched has a positive effect on the next submission grade
 * --> count the number of different videos (`NumberVideoWatched`)
* if the learner seeks to specific points in the video lectures, (s)he is actively engaged with the course material
 * --> count the number of seek events (`NumberOfSeekEvents`)

__Hypothese related to forum events__
* the number of threads viewed has a positive effect on the next submission grade
 * --> count the number of thread views (`NumberOfThreadViews`)
* the number of thread created has a positive effect on the next submission grade
 * --> count the number of thread launched (`NumberOfThreadCreated`)
* the number of comments posted has a positive effect on the next submission grade
 * --> count the number of comments posted (`NumberOfComments`)
* When a learner upvotes a post or a comment, most likely they found the contet helpful and it helped them solve their problems, this might have a positive effect on the next submission grade.
 * --> count the number of upvotes for both comments and posts (`NumberOfUpvotes`)
  
__Hypothese combining both events (bigrams and trigrams)__
* watching a video followed by posting

__Other hypotheses__
* the time between two submissions should be indicative of the grade difference. A lot of submissions with relatively small time durations between submissions reflect a "trial and error" pattern where the learner typically tests some lines of code and wants to see the result by submitting. This behaviour is prone to errors in the code and as such should have a negative effect on the grade.
*TODO (probably secondary features for regression task)
 * --> find out if certain sequences of behavior are good predictors of improvement
 * --> compute more in-depth representations of what happened on the forum (did someone reply to your forum thread? Did you reply to them?)
