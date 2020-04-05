# GitHub README Content Classifier

## What
This project contains the source code of GitHub README content classifier from the paper "Categorizing the Content of GitHub README Files" (Gede Artha Azriadi Prana, Christoph Treude, Ferdian Thung, Thushari Atapattu, David Lo), published in 2018 in Empirical Software Engineering. DOI: [10.1007/s10664-018-9660-3](https://link.springer.com/article/10.1007%2Fs10664-018-9660-3)

## Setup
This project is written in Python 3. It also uses SQLite to store intermediary data during processing. By default the database is  `database/data.db`.

The code requires creation of some directories for logging and temporary file storage. Please create these prior to running the scripts:
1. `log/`
2. `temp/abstracted_markdown/`
3. `temp/abstracted_html/`
4. `temp/target_abstracted_markdown/`

If you want to train a model using provided dataset to predict labels in new file that's not in the set, you'll also need to create the following directories:

5. `model/`. Used by `classifier_train_model.py` to save result of training. `classifier_classify_target.py` loads model saved in this directory for classifying sections in user-provided README file.
6. `input/clf_target_readmes/`. The default place to store README files whose section labels are to be predicted.
7. `output/`. Used by `classifier_classify_target.py` saves its resulting labels here.

## How to Use
The following sections describe three use cases and the steps to follow for each scenario. Before running each use case, empty the database using `empty_all_tables.py` .

### Use Case 1: Running Cross-validation Experiments
1. Set up file paths in `config/config.cfg`. By default, CSV files listing the section titles and their labels are in `input/`. `dataset_1.csv` contains the section titles and labels for the development set, whereas `dataset_2.csv` contains the section titles and labels for the evaluation set. The README files corresponding to the CSV files are in `input/ReadMes/` directory.
2. Load development (i.e. the 25% used to develop heuristics) and evaluation (i.e. the remaining 75%) datasets by running `script/load_dev_and_eval_datasets.py`
3. Run the `script/experiment/*` scripts as required. E.g. to run experiment comparing cross-validation result on different algorithms, run `script/experiment_classifier_validation.py`. 

### Use Case 2: Training Model on Existing Data and Classifying New Files
1. Run `script/load_combined_set_and_train_model` to extract and load contents and titles listed in combined development and evaluation sets into the database. This script by default reads `dataset_combined.csv` for section heading and labels, and the README files in `input/ReadMes/` directory for the section contents. 
2. Download the new README file(s) whose sections are to be labeled into a directory.
3. Open configuration file of the classifier (`config/config.cfg`), and edit the `target_readme_file_dir` variable to point to the location of the README file(s) to be labeled.
4. Run `script/load_and_classify_target` to extract contents of the new README files, load the section contents, and perform classification.
5. By default, the resulting section labels will be saved in `output/output_section_codes.csv`. Classifier will also identify which codes exist for each file, and which codes don't yet exist (i.e. potential for README expansion). This information will be saved in `output/output_file_codes.csv`

### Use Case 3: Training Model on Existing Data and Classifying New Files (More Detailed Breakdown)
Each script used in the previous section automates multiple steps in the workflow to make usage simpler. If you want more detailed breakdown, e.g. to facilitate evaluation of intermediary result after each step in the workflow, please use the following steps.

#### Training Model Using Existing Data
1. Run `script/load_section_dataset_combined.py`. This script extracts and loads section overview (title text, labels) from CSV file containing complete set of section headings and labels. In `config/config.cfg`, this CSV file is specified as `dataset_combined.csv` by default. The script also loads section content of the associated README files. All these data are subsequently stored in tables with name ending in `combined` in the database.
2. Run `script/classifier_train_model.py`. This script will train SVM model using the data in `*combined` database tables. The resulting model, TFIDF vectorizer, and matrix label binarizer will be saved in `model/` directory.
#### Loading New File
3. Download the new README file(s) whose sections are to be labeled into a directory.
4. Open configuration file of the classifier (`config/config.cfg`), and edit the `target_readme_file_dir` variable to point to the location of the README file(s) to be labeled.
5. Run `script/load_target_sections.py` to load the section heading and content data into database.
#### Classifying Sections in the New File
6. Run `script/classifier_classify_target.py`. This script will use the saved model, vectorizer, and binarizer to classify target README files in the directory specified in `target_readme_file_dir` variable in `config/config.cfg`. 
7. By default, the resulting section labels will be saved in `output/output_section_codes.csv`. Classifier will also identify which codes exist for each file, and which codes don't yet exist (i.e. potential for README expansion). This information will be saved in `output/output_file_codes.csv`

## Notes
All scripts will log output (such as F1 score, execution times) into `log/` directory. Preprocessed README files (with numbers, `mailto:` links etc. abstracted out) are saved in `temp/` directory. Patterns used for heuristics are listed in `doc/Patterns.ods`.
