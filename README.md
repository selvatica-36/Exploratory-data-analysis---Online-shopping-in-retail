# Exploratory Data Analysis (EDA): Online Shopping in Retail

[![Open in Visual Studio Code](https://img.shields.io/badge/Open%20in-Visual_Studio_Code-5C2D91?style=flat&logo=visual%20studio&logoColor=white)](https://open.vscode.dev/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail)  ![GitHub last commit](https://img.shields.io/github/last-commit/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail)  ![issues](https://img.shields.io/github/issues/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail.svg)

## Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  ![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)

## Project Description
✨ **Welcome** to this comprehensive end-to-end EDA project where we will uncover and analyse trends, patterns and anomalies in retail customer activity data. The dataset used here belongs to an anonymised multinational retail company (provided by AiCore), and contains yearly online sales data and general website performance data. 

🔭 **The first part of the project focuses on data exploration and cleaning.** To start, we will develop a simple ELT pipeline: the data will be extracted from an AWS RDS database, loaded as a dataframe and cleaned for analysis by transforming column data types and dealing with missing data. The data will also be prepared for ML by dealing with outliers, overly correlated columns and data skewness. 

📊 **The second part of the project focuses on data analysis to uncover business insights.** We will answer relevant business questions regarding sales trends, marketing strategy, website performance and customer behaviour. To do so, we will generate informative data visualisations and **offer insights and recommendations**.


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
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white) 




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