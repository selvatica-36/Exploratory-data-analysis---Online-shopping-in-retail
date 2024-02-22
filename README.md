# Exploratory Data Analysis (EDA): Online Shopping in Retail

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail)  ![GitHub last commit](https://img.shields.io/github/last-commit/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail) [![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail)


## Summary


## Table of Contents
1. [Introduction](#1-introduction)
2. [Installation instructions](#2-installation-instructions)
3. [Usage instructions](#3-usage-instructions)
4. [File structure](#4-file-structure)
5. [License information](#5-license-information)


## 1. Project Description
**As a learner**, my aim in this project was to consolidate my EDA knowledge, with a specific focus on OOP-oriented programming, data cleaning and visualisation. My main two learning points have been:
- Imputation of null values.
- Correcting skewness in dataset columns.
- Working with pandas to filter and group data. 

For the full information on all dataset variables and their meaning, please refer to the top of the analysis_report.ipynb file.

## 2. Technologies used






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


## 3. Usage instructions
To access the final report insights, please check analysis_report.ipynb directly.

## 4. File Structure

```
─ data
│   ├── cleaned_skewed_data.csv  #Cleaned data for analysis
│   ├── ML_preprocessed_data.csv #Cleaned and transformed data for ML 
│   └── customer_activity.csv #Data downloaded fron RDS database 
├── readme-images
│   └── EDA_flow_chart.png
├── scripts
│   ├── db_utils.py
│   ├── info_extractor.py
│   ├── outlier_detector.py
│   ├── plotter.py
│   ├── statistical_tests.py
│   └── transformer.py 
├── EDA_customer_activity.ipynb
├── business_analysis_report.ipynb
├── requirements.txt
├── environment.yml
├── .gitignore
├── README.md

```
## 5. License information
This is an open source public repository. The dataset was obtained from Aicore. AiCore provided the necessary credentials to download the dataset from AWS RDS.

![alt text](/readme-images/EDA_flow_chart.png)