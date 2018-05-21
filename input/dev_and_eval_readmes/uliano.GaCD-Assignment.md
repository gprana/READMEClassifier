GaCD-Assignment
===============
#`run_analysis.R` 
This script summarises (by taking the average) some of the features of the Samsung dataset (more details [here](http://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones)) into a tidy dataset and outputs it to `summary.txt` file.

It presumes to be in the same directory where the `UCI HAR Dataset` directory is, and to be run with the directory containing itself as R current working directory (if you `source()` it from elsewhere use the `'chdir = TRUE'` option).

It reads faeture names, corrects some typo and other uglyness in their names and finds the ones containing "Mean" od "Std".

Then it reads the data for the two datasets "Train" and "Test", assignes the corrected feature names to their column names and selects only the desired variables.

Columns for activity and subject are created reading the appropriate auxiliary files, first columns and then rows are binded to a single tidy dataset.

With the help of `dlpyr` package data are grouped by subject and activity and then averaged. The result is saved in the working directory as `summary.txt`

# `codebook.md`
is the codebook for `summary.txt`


