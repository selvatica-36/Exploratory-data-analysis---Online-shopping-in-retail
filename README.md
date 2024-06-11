# Exploratory Data Analysis (EDA): Online Shopping in Retail

[![Open in Visual Studio Code](https://img.shields.io/badge/Open%20in-Visual_Studio_Code-5C2D91?style=flat&logo=visual%20studio&logoColor=white)](https://open.vscode.dev/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail)  ![GitHub last commit](https://img.shields.io/github/last-commit/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail)  ![issues](https://img.shields.io/github/issues/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail.svg) ![Python version](https://img.shields.io/badge/Python%20version-3.12.1-FF9900?style=flat&logo=python&logoColor=white)

## Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-298D46?style=for-the-badge&logo=jupyter&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-5C2D91?style=for-the-badge) ![SQAlchemy](https://img.shields.io/badge/SQLAlchemy-FF5722?style=for-the-badge) ![Git](https://img.shields.io/badge/Git-B1361E?style=for-the-badge&logo=git&logoColor=white) ![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![VSCode](https://img.shields.io/badge/VSCode-2962FF?style=for-the-badge&logo=visual%20studio&logoColor=white)

## Executive Summary: 
In this project I uncovered trends and patterns in website transactional data from a multinational online retail company. Using Python, I extracted the data from AWS RDS, and then cleaned and transformed it for analysis and ML modelling. I performed exploratory data anlysis (EDA) on the dataset to uncover trends and patterns, and answered common questions from the sales and marketing teams. 

Focusing on the marketing strategy, I discovered that ads traffic are the second largest driver of revenue (after direct search), bringing 28% of sales, followed by social traffic (19%). After a detailed analysis on conversion rates, bounce rates and mobile vs. desktop usage, these are my recommendations:

1. Consider investing more in traffic with high conversion rates (20%+), such as affiliate marketing and youtube channels.

2. Improve mobile platform acessibility and increase investing into social traffic, simultaneously.

3. Review current costs/ad and campaign costs to evaluate whether to keep investing in current platforms. 


## Business Problem: 
This fictitious multinational company is a leader in online sales. They have hired a data team to keep track of website transactions and spot trends in sales and website anomalies. The website transactions are stored in AWS RDS.

## The Solution:
Perform **end-to-end exploratory data analysis (EDA)** to uncover and analyse trends, patterns and anomalies in **retail customer activity data**. The dataset used here belongs to an anonymised multinational retail company (provided by AiCore), and contains yearly online sales data and general website performance data.

The data needs to extracted from AWS RDS and saved locally before proceeding to data cleaning and exploration. Then I will proceed to answer business queries from the sales and marketing teams.

### Methodology

![alt text](/readme-images/EDA-Project.png)

1. **Data extraction and cleaning.** I developed an ELT pipeline: the data was be extracted from AWS RDS database, loaded as a dataframe and cleaned for analysis by transforming column data types and dealing with missing data. The data was also be prepared for ML by dealing with outliers, dropping overly correlated columns and correcting data skewness (log, boxcox transformations).

2. **Exploratory Data Analysis (EDA)**. I identified general trends in the data by looking at summary statistics, variable distributions and variable-variable relationships, and detected relevant anomalies. For data cleaning and EDA, please check the notebook [`EDA_website_activity.ipynb`](https://github.com/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail/blob/main/EDA_website_activity.ipynb).

3. **Explanatory Data Analysis.** relevant business questions regarding sales trends, marketing strategy, website performance and customer behaviour. To do so, I generated informative data visualisations and **offered insights and recommendations**. This is available in the notebook [`business_analysis_report.ipynb`](https://github.com/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail/blob/main/business_analysis_report.ipynb).

4. **Bonus**: conversion rate analysis using pivot tables in Excel.


### Skills

`Python`: Pandas, Numpy, SQLAlchemy, YAML, statsmodels, SciPy, matplotlib, seaborn, missingno, tabulate.

`Excel`: pivot tables, pivot charts (conversion rate analysis only)

### Case Study: Do we need to improve our marketing strategy? 

![alt text](/readme-images/marketing-strategy.png)

![alt text](/readme-images/marketing-strategy-2.png)

#### **More Insights**
- Google search traffic contributes the most to revenue across all regions (40-50%). Facebook ads is the second highest contributor in all regions except for South America, where Bing search takes second place. Trends are fairly similar across all regions.

![alt text](/readme-images/traffic_revenue_region.png)
- Youtube and Instagram ads have the highest bounce rates across the board. Google search, Instagram pages and Pinterest have the lowest bounce rates. Asia is an exception with Yahoo search having the highest bounce rate.

- November generated the most sales from ads traffic (11% of total sales), followed by May and December. February generated the least amount of sales from ads traffic (0.1%). Facebook ads generate the most sales across all months except for May, where instagram ads where most successful.

#### **Recommendations**

1️⃣ Spend less or cut Youtube ads. Youtube ads are not effective: they have the highest bounce rate and bring very little revenue.

2️⃣ Spend more on instagram ads. Instagram ads have the potential to bring more revenue: the bring about 10% of revenue, despite the high bounce rates. Out of all social ad platforms, instagram comes second every month except for May, where instagram ads where the most sucessful.

3️⃣ Increase budget in ads and social traffic. This should be done at the same time as increasing mobile accesibility to the website.

### Additional business recomendations 

1️⃣ Offer sales and discounts during February and June (lowest revenue months).

2️⃣ Offer discounts to weekend visitors to entice weekend sales, as well as to returning visitors.

3️⃣ **Improve mobile accessibility to the website.** Data shows most users access through desktop, which can indicate that the website does not work as well on mobile.

## Project set up and how-to guides
For detailed guides to the project, please refer to the [Github Wiki](https://github.com/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail/wiki). These guides include installation instructions, how to use the repository and details on the dataset. 

## Improvements and next steps 
- YoY growth analysis (in number of sales).
- Investigate better ways of imputing data (if applicable): regression, MICE, KNN, etc.
- Classification model to analyse whether certain factors are predictors of revenue.

## File Structure
```
├──data
│   ├── customer_web_data_clean.csv  #Cleaned data for analysis
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
├── EDA_website_activity.ipynb
├── business_analysis_report.ipynb
├── conversion_rate_analysis.xlsx
├── requirements.txt
├── environment.yml
├── .gitignore
├── README.md

```

## License information
This is an open source public repository. The dataset was obtained from Aicore. AiCore provided the necessary credentials to download the dataset from AWS RDS (these are not publicly available).
