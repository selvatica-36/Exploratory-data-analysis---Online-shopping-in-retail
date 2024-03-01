# Exploratory Data Analysis (EDA): Online Shopping in Retail

[![Open in Visual Studio Code](https://img.shields.io/badge/Open%20in-Visual_Studio_Code-5C2D91?style=flat&logo=visual%20studio&logoColor=white)](https://open.vscode.dev/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail)  ![GitHub last commit](https://img.shields.io/github/last-commit/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail)  ![issues](https://img.shields.io/github/issues/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail.svg) ![Python version](https://img.shields.io/badge/Python%20version-3.12.1-FF9900?style=flat&logo=python&logoColor=white)

## Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-298D46?style=for-the-badge&logo=jupyter&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-5C2D91?style=for-the-badge) ![SQAlchemy](https://img.shields.io/badge/SQLAlchemy-FF5722?style=for-the-badge) ![Git](https://img.shields.io/badge/Git-B1361E?style=for-the-badge&logo=git&logoColor=white) ![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![VSCode](https://img.shields.io/badge/VSCode-2962FF?style=for-the-badge&logo=visual%20studio&logoColor=white)


## Project Description
✨ **Welcome** to this comprehensive **end-to-end EDA project** where we will uncover and analyse trends, patterns and anomalies in **retail customer activity data**. The dataset used here belongs to an anonymised multinational retail company (provided by AiCore), and contains yearly online sales data and general website performance data. 

🔭 **The first part of the project focuses on data exploration and cleaning.** We will first develop an ELT pipeline: the data will be extracted from an AWS RDS database, loaded as a dataframe and cleaned for analysis by transforming column data types and dealing with missing data. The data will also be prepared for ML by dealing with outliers, overly correlated columns and data skewness. 

📊 **The second part of the project focuses on data analysis to uncover business insights.** We will answer relevant business questions regarding sales trends, marketing strategy, website performance and customer behaviour. To do so, we will generate informative data visualisations and **offer insights and recommendations**.

## Project set up and instructions
For detailed guides to the project, please refer to the [Github Wiki](https://github.com/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail/wiki).These guides include installation instructions, how to use the repository and details on the dataset. 

## Currently working on
- Developing a data story and case analysis study to include in this README file. This will involve a rewrite of the section below: **Business insights and recommendations**. *Please, come back again soon!*

## Improvements and next steps
- Perform hypothesis testing: run 2-sample t-tests in certain parts of the analysis to determine wether the differences between groups are significant or not. 
- Further deep dive into data missingness mechanisms to determine if imputation was done in the best way.
- Investigate better ways of imputing data (if applicable): regression, MICE, KNN, etc.

## Business insights and recommendations
For the full exploratory data analysis (EDA), please check the notebook [`EDA_customer_activity.ipynb`](https://github.com/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail/blob/main/EDA_customer_activity.ipynb).
For the full business analysis, please check the notebook [`business_analysis_report.ipynb`](https://github.com/selvatica-36/Exploratory-data-analysis---Online-shopping-in-retail/blob/main/business_analysis_report.ipynb).

### 6.1. What are our customers doing?
#### **Insights**
GENERAL SALES
- 77% of total sales happen during the week, whereas 23 % of total sales happen on the weekend.
- 39% of total sales happen in North America, followed by 17% in Western Europe. Oceania is the weakest market, making up 2.6% of total sales.
- Google search brings more than 45% of total revenue, followed by Facebook ads (12%). Tiktok ads and facebook pages are amongst the least successful.
- November is the month with the most revenue (38%) followed by May (17.5%). February and June are bring the least revenue (<1%).

<div style="text-align: center;">
<img src="./readme-images/example_visualisation_1.png" class ="displayed" width="400" height="300" />
</div>

WEBSITE ACTIVITY
-  Per visit, a user spends 89% of their time in product-related tasks, 8.7% in administrative tasks and 2.2% on informational tasks, on average. 
    - There are a total of 296 product-related tasks, 24 administrative tasks and 13 informational tasks.
    - The total amount of hours spent by all users combined in each task are:
        - 4047 hours in product-related tasks.
        - 269.5 hours in administrative tasks.
        - 114.5 hours in informational tasks.
- On average, users spents most time doing administrative tasks '21' and '17', and informational tasks '8' and '10'. However, there is **high variability** in the most pupular tasks amongst the user base.

#### **Recommendations**

1️⃣ Offer sales and discounts during February and June.

2️⃣ Increase advertising budget on TikTok and Instagram as they are more frequently used than facebook.

### 6.2. What software are our customers using the most to access the website?
#### **Insights**
OERATING SYSTEMS AND DEVICES
- The three most used operating systems are: Windows (53.5%), MacOS (21.7%) and Android (21%). The least used systems are Ubuntu (0.07%) and ChromeOS (0.05%). **Out of the mainstream systems, iOS only takes 3%.**
- 76% of users access the website through desktop and **24% via mobile.**
- Breakdown of OS usage by region: trend seems to be consistent across all regions.

![alt text](/readme-images/example2.png)

BROWSER SUPPORT
- The three most used browsers are: Google Chrome (65.6%), Safari (20.5%) and Mozilla Firefox (6.7%). **All three were accessed more often through desktop than mobile** (60-95% of the time).
- Minimal impact: The only browser that was accessed more often via mobile was Android (0.98% of visits), with 95% of Android users accessing via mobile.

<div style="text-align: center;">
<img src="./readme-images/browser_device.png" class ="displayed" width="400" height="300" />
</div>

#### **Recommendations**

1️⃣ **Improve mobile accessibility to the website.** Data shows most users access through desktop, which can indicate that the website does not work as well on mobile.

### 6.3. Do we need to optimise the marketing strategy?
#### **Insights**
- Google search traffic contributes the most to revenue across all regions (40-50%). Facebook ads is the second highest contributor in all regions except for South America, where Bing search takes second place. Trends are fairly similar across all regions.

![alt text](/readme-images/traffic_revenue_region.png)
- Youtube and Instagram ads have the highest bounce rates across the board. Google search, Instagram pages and Pinterest have the lowest bounce rates. Asia is an exception with Yahoo search having the highest bounce rate.

- November generated the most sales from ads traffic (11% of total sales), followed by May and December. February generated the least amount of sales from ads traffic (0.1%). Facebook ads generate the most sales across all months except for May, where instagram ads where most successful.

<div style="text-align: center;">
<img src="./readme-images/traffic_ads_revenue.png" class ="displayed" width="400" height="300" />
</div>

#### **Recommendations**

1️⃣ Spend less or cut Youtube ads. Youtube ads are not effective: they have the highest bounce rate and bring very little revenue.

2️⃣ Spend more on instagram ads. Instagram ads have the potential to bring more revenue: the bring about 10% of revenue, despite the high bounce rates. Out of all sial ad platforms, instagram comes second every month except for May, where instagram ads where the most sucessful.

3️⃣ Keep investing on instagram pages. They are effective (low bounce rates) even if they only bring < 5 % of revenue.

### 6.4. Detailed sales breakdown
#### **Insights**
NEW VS. RETURNING VISITORS
 - Most purchases are made by returning visitors (79.5%). 
 - Returning visitors make up 86.7% of total visitors. Out of all returning visitors, 14% of them make a purchase.
 - Out of all new visitors, 24% of them make a purchase.

WEEK VS. WEEKEND SALES
 - The percentage of visitors making a purchase on the weekend (16.9%) is marginally higher than the percentage of visitors making a purchase during the week (15%). However, as we analysed in Part 1, most sales happen during the week (77%) because the number of total visitors Monday-Friday is x3.8 times higher than during the weekend.

TRAFFIC TYPE CONTRIBUTION TO SALES
- Search traffic is contributing the most to total sales (55%), followed by ads traffic (27.7%), social traffic (15.9%) and direct traffic (1.3%).

#### **Recommendations**

1️⃣ Offer rewards and discounts for returning visitors. 

2️⃣ Offer discounts to weekend visitors to entice weekend sales. 

3️⃣ Increase budget in ads and social traffic. This should be done at the same time as increasing mobile accesibility to the website. 

## File Structure
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

## License information
This is an open source public repository. The dataset was obtained from Aicore. AiCore provided the necessary credentials to download the dataset from AWS RDS (these are not publicly available).
