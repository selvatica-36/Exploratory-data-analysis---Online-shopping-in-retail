# EDA: Online Shopping in Retail
## Summary
In this project, I have performed exploratory data analysis on a sample retail industry dataset, detailing website information for every visitor.

## Table of Contents
1. [Introduction](#1-introduction)
2. [Installation instructions](#2-installation-instructions)
3. [Usage instructions](#3-usage-instructions)
4. [File structure](#4-file-structure)
5. [License information](#5-license-information)


## 1. Introduction
**As a learner**, my aim in this project was to consolidate my EDA knowledge, with a specific focus on OOP-oriented programming, data cleaning and visualisation. My main two learning points have been:
- Imputation of null values.
- Correcting skewness in dataset columns.
- Working with pandas to filter and group data. 

For the full information on all dataset variables and their meaning, please refer to the top of the analysis_report.ipynb file.

## 2. Installation instructions
All files are stored remotely in Github: https://github.com/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail

The repository contains:
- This README.md file
- .gitignore
- db_utils.py: Contains utility class and methods to connect to AWS RDS and download the dataset locally. 
- data_utils.py: Contains classes with utility functions, to extract dataframe information, perform transformations and produce plots. 
- EDA_customer_activity.ipynb: Notebook containing the data preprocessing steps: handling of nulls, skewness and collinearity.
- analysis_report.ipynb: Notebook containing the final analysis and visualisations, in response to various queries  of interest.
- The dataset files:
    - 'customer_activity.csv': Raw dataset downloaded from RDS
    - 'data_preprocessed.csv': preprocessed dataset including all transformations performed in 'EDA_customer_activity.ipynb'
    - 'data_preprocessed_skewed': preprocessed dataset, including only handling of nulls. No columns have been transformed or deleted.

NOTE: the user should have conda or pip installed with a python package (python version 3.11.5).

## 3. Usage instructions
To access the final report insights, please check analysis_report.ipynb directly.


## 5. License information
This is an open source public repository. The dataset was obtained from Aicore. 