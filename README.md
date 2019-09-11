# GitHub README Content Classifier

## What
This project contains the source code of GitHub README content classifier from the paper "Categorizing the Content of GitHub README Files" (Gede Artha Azriadi Prana, Christoph Treude, Ferdian Thung, Thushari Atapattu, David Lo), published in 2018 in Empirical Software Engineering. DOI: [10.1007/s10664-018-9660-3](https://link.springer.com/article/10.1007%2Fs10664-018-9660-3)

## How to Use
This project is written in Python 3. It also uses SQLite to store intermediary data during processing. By default the database is  `database/data.db`.

### Cross-validation Experiments
1. Set up file paths in `config/config.cfg`. By default, CSV files listing the section titles and their labels are in `input/`. `dataset_1.csv` contains the section titles and labels for the development set, whereas `dataset_2.csv` contains the section titles and labels for the evaluation set. The README files corresponding to the CSV files are in `input/ReadMes/` directory. 
2. Empty all database tables by running the script `script/loading/empty_all_tables.py`
3. Run `script/loading/load_section_dataset_25pct.py` to extract and load section overview (title text, labels) and content of development set into database.
4. Run `script/loading/load_section_dataset_75pct.py` to extract and load section overview (title text, labels) and content of evaluation set into database. 
5. Run the `script/experiment/*` scripts as required. E.g. `script/experiment/classifier_75pct_tfidf.py` for the SVM version. 

Note that `25pct` and `75pct` in script names refer to development and evaluation sets, respectively. Before running an experiment, please ensure that you've loaded the correct set.

### Training Model on Existing Data and Classifying New Files
1. Run `script/classifier/load_combined_set_and_train_model` to extract and load contents and titles listed in combined development and evaluation sets (by default, defined as `dataset_combined.csv` in `config/config.cfg`) into the database.
2. Download the new README file(s) whose sections are to be labeled into a directory.
3. Open configuration file of the classifier (`config/config.cfg`), and edit the `target_readme_file_dir` variable to point to the location of the README file(s) to be labeled.
3. Run `script/classifier/load_and_classify_target` to extract contents of the new README files, load the section contents, and perform classification.
4. By default, the resulting section labels will be saved in `output/output_section_codes.csv`. Classifier will also identify which codes exist for each file, and which codes don't yet exist (i.e. potential for README expansion). This information will be saved in `output/output_file_codes.csv`

### Training Model on Existing Data and Classifying New Files (More Detailed Breakdown)
Each script used in the previous section automates multiple steps in the workflow to make usage simpler. If you want more detailed breakdown, e.g. to facilitate evaluation of intermediary result after each step in the workflow, please use the following steps.

#### Training Model Using Existing Data
1. Run `script/loading/load_section_dataset_combined.py` to extract and load section overview (title text, labels) and content of combined development and evaluation sets (by default, defined as `dataset_combined.csv` in `config/config.cfg`) into the database. 
2. Run `script/classifier/classifier_train_model.py`. This script will train SVM model using combined dataset in `*combined` tables. The resulting model, TFIDF vectorizer, and matrix label binarizer will be saved in `model/` directory.
#### Loading New File
3. Download the new README file(s) whose sections are to be labeled into a directory.
4. Open configuration file of the classifier (`config/config.cfg`), and edit the `target_readme_file_dir` variable to point to the location of the README file(s) to be labeled.
5. Run `script/loading/load_target_section_data.py` to load the section heading and content data into database.
#### Classifying Sections in the New File
6. Run `script/classifier/classifier_classify_target.py`. This script will use the saved model, vectorizer, and binarizer to classify target README files in the directory specified in `target_readme_file_dir` variable in `config/config.cfg`. 
7. By default, the resulting section labels will be saved in `output/output_section_codes.csv`. Classifier will also identify which codes exist for each file, and which codes don't yet exist (i.e. potential for README expansion). This information will be saved in `output/output_file_codes.csv`

## Notes
All scripts will log output (such as F1 score, execution times) into `log/` directory. Preprocessed README files (with numbers, `mailto:` links etc. abstracted out) are saved in `temp/` directory. Patterns used for heuristics are listed in `doc/Patterns.ods`.
