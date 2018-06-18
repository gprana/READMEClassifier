# GitHub README Content Classifier

## What
This project contains the source code of GitHub README content classifier from "Categorizing the Content of GitHub README Files" (Gede Artha Azriadi Prana, Christoph Treude, Ferdian Thung, Thushari Atapattu, David Lo).

## How to Use
This project is written in Python 3.

### Preparation
1. Set up file paths in `config/config.cfg`. By default, CSV files listing the section titles and their labels are in `input/` (`dataset_1.csv` contains the section titles and labels for the development set, whereas `dataset_2.csv` contains the section titles and labels for the evaluation set). The README files corresponding to the CSV files are in `input/ReadMes/` directory. 
2. Empty all database tables by running the script `script/loading/empty_all_tables.py`
3. Run `script/loading/load_section_dataset_25pct.py` to extract and load section overview (title text, labels) and content of development set into database.
4. Run `script/loading/load_section_dataset_75pct.py` to extract and load section overview (title text, labels) and content of evaluation set into database. 

### Training Model and Classifying Files
1. Place the README files whose sections are to be classified in the directory specified in `target_readme_file_dir` variable in `config/config.cfg`.
2. Run `script/loading/load_target_section_data.py` to load the section heading and content data into database.
3. Run `script/classifier/classifier_train_model.py`. This script will train SVM model using combined development and evaluation dataset. The resulting model, TFIDF vectorizer, and matrix label binarizer will be saved in `model/` directory.
4. Run `script/classifier/classifier_classify_target.py`. This script will use the saved model, vectorizer, and binarizer to classify target README files in the directory specified in `target_readme_file_dir` variable in `config/config.cfg`. By default, the resulting labels will be saved in `output/output.csv`

### Running 10-fold Cross Validation Experiments
1. Run the `script/experiment/*` scripts as required. E.g. `script/experiment/classifier_75pct_tfidf.py` for the SVM version.

## Notes
All scripts will log output (such as F1 score, execution times) into `log/` directory. Preprocessed README files (with numbers, `mailto:` links etc. abstracted out) are saved in `temp/` directory. Patterns used for heuristics are listed in `doc/Patterns.ods`.