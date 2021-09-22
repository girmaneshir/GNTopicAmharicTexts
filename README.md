# Amharic Topic Detection

This is a Python program that does Topic Detection of Amharic Texts.

The program consists of different components and three experimental settings. And three feature sets (LDA, TF-IDF and combinations of LDA and TFIDF) are used in those experiments.

(1) preprocessing (cleaning data, tokenize, numeral removal, normalization, stop word removal)
(2) Exp. I   (WithNo Stemming)
(3) Exp. II  (With Stemming)
(4) Exp. III (With SMOTE)

## Requirments

Install anaconda and create vritual environment
Make sure installing Python 3 and above`from anaconda
Install necessary library files for machine learning : scikit learn, pandas, imblearn, etc.


## How to test
 (1) Download and extract zip files which contains (jupyter notebook, datasets, support files)
 (2) Download the data set from ""doi:10.5281/zenodo.5504175""
 (3) Change anaconda virtual env. and open "jupyter notebook" from the command line
 (4) Upload jupyter notebook file named"Amharic_Topic_Modeling_for_Amharic_User_Generated_Texts_SEPT2021_MDPI.ipynb" from your browser of jupyter local server
 (5) Change the directory of the support code .py files such as "Amharic_stemmer_Tilahun_API.py" and "amharic_normalization_api.py" and data set(doi:10.5281/zenodo.5504175) of jupter notebook code by the directories of the coresponding files (in step 1) on which they are located on your computer
 (6) Enjoy testing it!


## How to cite
 You can cite this source "Neshir, Girma. Corpus for Amharic Topic Classification. 2021, doi:10.5281/zenodo.5504175."
