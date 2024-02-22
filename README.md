# Exploratory Data Analysis (EDA): Online Shopping in Retail

[![Open in Visual Studio Code](https://img.shields.io/badge/Open%20in-Visual_Studio_Code-5C2D91?style=flat&logo=visual%20studio&logoColor=white)](https://open.vscode.dev/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail)  ![GitHub last commit](https://img.shields.io/github/last-commit/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail)  ![issues](https://img.shields.io/github/issues/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail.svg) ![Python version](https://img.shields.io/badge/Python%20version-3.12.1-FF9900?style=flat&logo=python&logoColor=white)

## Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-298D46?style=for-the-badge&logo=jupyter&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-5C2D91?style=for-the-badge) ![SQAlchemy](https://img.shields.io/badge/SQLAlchemy-FF5722?style=for-the-badge) ![Git](https://img.shields.io/badge/Git-B1361E?style=for-the-badge&logo=git&logoColor=white) ![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![VSCode](https://img.shields.io/badge/VSCode-2962FF?style=for-the-badge&logo=visual%20studio&logoColor=white)


## Project Description
✨ **Welcome** to this comprehensive **end-to-end EDA project** where we will uncover and analyse trends, patterns and anomalies in **retail customer activity data**. The dataset used here belongs to an anonymised multinational retail company (provided by AiCore), and contains yearly online sales data and general website performance data. 

🔭 **The first part of the project focuses on data exploration and cleaning.** We will first develop an ELT pipeline: the data will be extracted from an AWS RDS database, loaded as a dataframe and cleaned for analysis by transforming column data types and dealing with missing data. The data will also be prepared for ML by dealing with outliers, overly correlated columns and data skewness. 

📊 **The second part of the project focuses on data analysis to uncover business insights.** We will answer relevant business questions regarding sales trends, marketing strategy, website performance and customer behaviour. To do so, we will generate informative data visualisations and **offer insights and recommendations**.


## Table of Contents
1. [Installation instructions](#1-installation-instructions)
3. [Usage instructions](#3-usage-instructions)
4. [File structure](#4-file-structure)
5. [License information](#5-license-information)

## 1. Installation instructions
All needed files are stored in this Github repo: https://github.com/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail

This project has been developed within a custom conda environment. Upon creating the environment, I installed `pip` and then used `pip install` command to download from the PyPI library all modules and dependencies needed for the project. 

1. All environment requirements have been uploaded to the repo in two different formats: `environment.yml` and `requirements.txt`. Depending on your OS and/or your preference of virtual environment, you will need one or the other. 

    1a. To install environment into a python virtual environment, run: `pip install -r requirements.txt`

    1b. To install environment into a conda virtual environment, run: `conda env create --name environment_name -f environment.yml`

2. Clone repo locally and/or fork it to a separate github account.
3. Run scripts/notebooks as needed.

## 2. Technologies, modules and libraries 

### 2.1. Technologies

- **AWS**: Used for cloud-based services and storage.
- **Jupyter Notebooks**: Used for data exploration and analysis.

### 2.2. Python modules and libraries

`pandas`: fast, powerful, flexible and easy to use open source data analysis and manipulation tool.

`sqlalchemy`: toolkit for SQL interaction and an Object-Relational Mapping (ORM) library for database operations.

`numpy`: library that provides powerful and versatile array computations, mathematical functions and other tools for data analysis and visualisation.

`matplotlib`: library for creating static, animated, and interactive visualizations in Python.

`seaborn`: library for making statistical graphics in Python. It builds on top of matplotlib and integrates closely with pandas data structures.

`scipy.stats`: SciPy is a collection of mathematical algorithms and convenience functions built on NumPy. `stats` is a subpackage that provides statistical distributions and functions.

`statsmodels`: library that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration.

`missingno`: library that provides a series of visualisations to understance the presence and distributions of missing data within a pandas dataframe.

`math`: module that provides access to the mathematical functions.

`tabulate`: library and a command-line utility to pretty-print tabular data in Python.

`yaml`: library for working with YAML files.

`os`: module that provides a portable way of using operating system dependent functionality e.g. save a downloaded file on a local folder.

## 3. Understanding the dataset
### *Online customer activity in a multinational retail company*

| Column name               | Column description                                                                                                                                     |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|  administrative           |  Columns which indicates which administrative activity the user was performing on their account. Encoded as a number.                                                       |
|  administrative_duration  |  How long a user performed administrative tasks in that session.                                                                                       |
|  informational            |  Indicates which informational activity the user was performing on the website. Encoded as a number.                                                                        |
|  informational_duration   |  How long a users performed informational tasks in seconds during that session.                                                                        |
|  product_related          |  Indicates which product the user was viewing on the website. Encoded as a number.                                                                                          |
|  product_related_duration |  How long a user browsed products during that session.                                                                                                 |
|  bounce_rates             |  Historical bounce rate of that particular page for all users. They visited the directly and immediately exited. Heavily correlated with 'exit_rates'. |
|  exit_rates               |  Historical exit rate of the users from that particular page.                                                                                          |
|  page_values              |  The average value contribution of a page to a customer sale                                                                                           |
|  month                    |  Month the users activity took place                                                                                                                   |
|  operating_systems        |  Operating system the user was using                                                                                                                   |
|  browser                  |  The browser used by the user                                                                                                                          |
|  region                   |  The region the user originated from                                                                                                                   |
|  traffic_type             |  How the user was redirected to the site                                                                                                               |
|  visitor_type             |  Whether a customer was is new/returning or other                                                                                                      |
|  weekend                  |  Whether the activity only took place during the weekend                                                                                               |
|  revenue                  |  Whether the customer purchased anything that session                                                                                                  |


## 4. Project workflow: ELT & EDA Pipeline



![alt text](/readme-images/EDA_flow_chart.png)


## 5. Business insights and recommendations

## 4. File structure

```
├──data
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


## 5. License information
This is an open source public repository. The dataset was obtained from Aicore. AiCore provided the necessary credentials to download the dataset from AWS RDS (these are not publicly available).
