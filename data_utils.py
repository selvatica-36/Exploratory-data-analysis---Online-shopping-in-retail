from scipy import stats
from scipy.stats import chi2_contingency, normaltest
from statsmodels.graphics.gofplots import qqplot
from typing import Optional, List
import missingno as msno
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns
# NOTE Nice well ordered import statements here. Just remove the ones that aren't used.


class DataFrameInfo:
    """
    Initialize the DataFrameInfo object with a DataFrame.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame to analyze.

    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        Initialize the DataFrameInfo object with a DataFrame.

        Parameters:
        - dataframe (pd.DataFrame): The DataFrame to analyze.

        """
        self.df = dataframe.copy()

    def get_slice(self, columns=None) -> pd.DataFrame:
        """
        Get a subset of the DataFrame based on specified columns.

        Parameters:
        - columns: Columns to include in the subset. Can be provided as 
                   a list of column names formatted as string,
                   as a string if only one column is chosen, 
                   or as a tuple or two integers indicating the positions of the columns in the dataframe.
                   If a tuple is provided, the counting starts from zero. 
                   The second integer in the tuple is inclusive (see examples below). 

        Returns:
        - pd.DataFrame: A subset of the DataFrame. Returns the full DataFrame if columns=None

        Examples:
        ```
        # Returns columns named 'column1' and 'column2':
        subset = df_info.get_slice(['column1', 'column2']) 

        # Returns column named 'column1' only
        subset = df_info.get_slice('column1') 

        # Returns the first three columns of the dataframe (column with index 2 is included)
        subset = df_info.get_slice((0,2)) 
        ```

        """
        # NOTE Like this slicing feature to analyse subsets of the data really nice
        if columns is not None:
            try:
                if isinstance(columns, list): # slice by column names
                    columns = [col.lower() for col in columns]
                    return self.df[columns]
                elif isinstance(columns, str): # choose one column only, allows for string outside list
                    columns = columns.lower()
                    return self.df[[columns]]
                elif isinstance(columns, tuple) and len(columns) == 2 and all(isinstance(col, int) for col in columns):
                    return self.df.iloc[:, columns[0]:columns[1] + 1]
                else:
                    raise ValueError
            # NOTE Great use of exception handling here very nice indeed
            except KeyError as ke:
                print(f"KeyError: you need to provide a valid column name: {ke}")
            except ValueError as ve: 
                print(f"ERROR: Invalid columns parameter. Use a list of valid column names formatted as strings, " \
                      + f"or a numerical interval formatted as a tuple e.g. (0,3): {ve}")
            except AttributeError as ae:
                print(f"ERROR: Invalid columns parameter. Use a list of valid column names formatted as strings, " \
                      f"or a numerical interval formatted as a tuple e.g. (0,3): {ae}")
        else:
            return self.df
        
    def extract_column_names(self, columns=None) -> List[str]:
        """
        Extract column names from a subset of the DataFrame.

        Parameters:
        - columns: Columns to include in the subset. 
        See docs for get_slice method for the requirements of the 'columns' parameter > help(get_slice)

        Returns:
        - List[str]: List of column names.

        Example:
        ```
        column_names = df_info.extract_column_names(['column1', 'column2'])
        ```

        """
        subset = self.get_slice(columns)
        return list(subset.columns)
    
    def data_types_columns(self, columns=None) -> pd.Series:
        """
        Get data types of columns in a subset of the DataFrame.

        Parameters:
        - columns: Columns to include in the subset.
        See docs for get_slice method for the requirements of the 'columns' parameter > help(get_slice)

        Returns:
        - pd.Series: Data types of columns.

        Example:
        ```
        dtypes = df_info.data_types_columns(['column1', 'column2'])
        ```

        """
        subset = self.get_slice(columns)
        return subset.dtypes
    
    def info_columns(self, columns=None) -> None:
        """
        Display concise information about columns in a subset of the DataFrame.

        Parameters:
        - columns: Columns to include in the subset.
        See docs for get_slice method for the requirements of the 'columns' parameter > help(get_slice)

        Example:
        ```
        df_info.info_columns(['column1', 'column2'])
        ```

        """
        subset = self.get_slice(columns)
        return subset.info()
    
    def extract_statistical_values(self, columns=None) -> pd.DataFrame:
        """
        Extract statistical values from columns in a subset of the DataFrame.

        Parameters:
        - columns: Columns to include in the subset.
        See docs for get_slice method for the requirements of the 'columns' parameter > help(get_slice)

        Returns:
        - pd.DataFrame: Statistical values of columns.

        Example:
        ```
        stats = df_info.extract_statistical_values(['column1', 'column2'])
        ```

        """
        subset = self.get_slice(columns)
        return subset.describe()
    
    def show_distinct_values(self,columns=None) -> None:
        """
        Display distinct values in columns of a subset of the DataFrame.

        Parameters:
        - columns: Columns to include in the subset.
        See docs for get_slice method for the requirements of the 'columns' parameter > help(get_slice)

        Example:
        ```
        df_info.show_distinct_values(['column1', 'column2'])
        ```

        """
        subset = self.get_slice(columns)
        for column in subset:
            try:
                print(f"Unique values in {column}:", np.sort(self.df[column].unique()))
            except TypeError:
                print(f"Unique values in {column}:", self.df[column].unique())

    def count_distinct_values(self, columns=None) -> pd.DataFrame:
        """
        Count distinct values in columns of a subset of the DataFrame.

        Parameters:
        - columns: Columns to include in the subset.
        See docs for get_slice method for the requirements of the 'columns' parameter > help(get_slice)

        Returns:
        - pd.DataFrame: Count of distinct values in columns.

        Example:
        ```
        counts = df_info.count_distinct_values(['column1', 'column2'])
        ```

        """
        subset = self.get_slice(columns)
        distinct_counts = pd.DataFrame({
            'column': subset.columns,
            'distinct_values_count': [subset[column].nunique() for column in subset.columns]
        })
        distinct_counts.set_index(['column'], inplace=True)
        return distinct_counts
    
    def print_shape(self, columns=None) -> None:
        """
        Print the shape of a subset of the DataFrame.

        Parameters:
        - columns: Columns to include in the subset.
        See docs for get_slice method for the requirements of the 'columns' parameter > help(get_slice)

        Example:
        ```
        df_info.print_shape(['column1', 'column2'])
        ```

        """
        subset = self.get_slice(columns)
        print("DataFrame Shape:", subset.shape)

    def generate_null_counts(self, columns=None) -> pd.DataFrame:
        """
        Generate null counts and percentages in columns of a subset of the DataFrame.

        Parameters:
        - columns: Columns to include in the subset.
        See docs for get_slice method for the requirements of the 'columns' parameter > help(get_slice)

        Returns:
        - pd.DataFrame: Null counts and percentages in columns.

        Example:
        ```
        null_info = df_info.generate_null_counts(['column1', 'column2'])
        ```

        """
        subset = self.get_slice(columns)
        null_counts = subset.isnull().sum()
        null_percentages = (null_counts / len(subset)) * 100
        null_info = pd.DataFrame({
            'null_count': null_counts,
            'null_percentage': null_percentages
        })
        return null_info
    
    def extract_numeric_features(self) -> pd.DataFrame:
        """
        Extract numeric features from the DataFrame.

        Returns:
        - pd.DataFrame: Numeric features.

        Example:
        ```
        numeric_features = df_info.extract_numeric_features()
        ```

        """
        numeric_features = self.df.select_dtypes(include=np.number)
        return numeric_features
    
    def extract_categorical_features(self, numeric_features: Optional[List[str]] = None) -> List[str]:
        """
        Extract categorical features from the DataFrame.

        Parameters:
        - numeric_features (Optional[List[str]]): List of numeric features (if already extracted).

        Returns:
        - List[str]: Categorical features.

        Example:
        ```
        categorical_features = df_info.extract_categorical_features(numeric_features=['num1', 'num2'])
        ```

        """
        if numeric_features is not None:
            categorical_features = [col for col in self.df.columns if col not in numeric_features]
            return categorical_features
        else:
            numeric_features = self.extract_numeric_features()
            categorical_features = [col for col in self.df.columns if col not in numeric_features]
            return categorical_features
        
    def print_summary_statistics(self, column_name: str) -> None:
        """
        Print summary statistics for a specific column.

        Parameters:
        - column_name (str): Name of the column.

        Example:
        ```
        df_info.print_summary_statistics('column1')
        ```

        """
        print(f"The mode of the distribution is {self.df[column_name].mode()[0]}")
        print(f"The mean of the distribution is {self.df[column_name].mean()}")
        print(f"The median of the distribution is {self.df[column_name].median()}")


class DataTransform:
        

        def __init__(self, dataframe):
            self.df = dataframe.copy()

        def convert_to_type(self, column_name, data_type, ignore_errors=True):
            data_type = data_type.lower()
            if ignore_errors == True:
                error_statement = ["coerce", "ignore"]
            elif ignore_errors == False:
                error_statement = ["raise", "raise"]
            else:
                print("Error: the parameter 'ignore_errors' is a bool and can only be True or False.")
            # Convert column to datatype:
            try:
                if data_type in ["datetime", "date"]:
                    self.df[column_name] = pd.to_datetime(self.df[column_name], errors=error_statement[0])
                elif data_type in ["str", "int", "float", "bool", "int64", "float64"]:
                    data_type = data_type.replace("64", "")
                    self.df[column_name] = self.df[column_name].astype(data_type, errors=error_statement[1])
                elif data_type == "categorical":
                    self.df[column_name] = pd.Categorical(self.df[column_name])
                else:
                    print(f"Error: data type {data_type} not supported. Check docstrings or call help for more information.")
            except Exception as e:
                print(f"Error converting column '{column_name}' to type '{data_type}': {e}")
            # TODO You could move a lot of what is in the this method to a dictionary mapping of the function and datatypes
            # it will keep your code cleaner but I really like the idea. 
            # you could reduce the size of the this method but place the conversion part of the code in another method and calling it here.
            # There are other ways to do this with dictionaries as well but it should reduce the overall size of your method doing it this way

        def convert_month_to_period(self, column_name):
            try:
                self.df[column_name] = self.df[column_name].astype(str)
                self.df['month'] = self.df['month'].str.lower()
                # NOTE I would actually move your mappings into a separate file here and import it just to keep it cleaner
                month_map = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'june': 6,
                            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
                self.df[column_name] = self.df[column_name].map(month_map)
                self.df[column_name] = pd.to_datetime(self.df[column_name], format='%m', errors='coerce').dt.to_period('M')
            except Exception as e:
                print(f"Error converting 'month' column to period: {e}")
            return self.df.copy()
        
        def convert_columns(self, column_list, data_type, ignore_errors=True):
            for column in column_list:
                self.convert_to_type(column, data_type, ignore_errors)
            return self.df.copy()
        
        def impute_nulls(self, column_list: List[str], method: str) -> pd.DataFrame:
            """
            Impute null values in specified columns using a specified method.

            Parameters:
            - column_list (List[str]): List of column names to impute null values.
            - method (str): Imputation method ('mean', 'median', or 'mode').

            Returns:
            - pd.DataFrame: A copy of the DataFrame with null values imputed.

            Example:
            ```
            df = your_instance.impute_nulls(['column1', 'column2'], 'mean')
            ```

            """
            method = method.lower()
            valid_methods = ['mean', 'median', 'mode']

            try:
                if method not in valid_methods:
                    raise ValueError(f"Invalid imputation method. Method can only be one of: {', '.join(valid_methods)}")

                for column in column_list:
                    if method == 'median':
                        self.df[column] = self.df[column].fillna(self.df[column].median())
                    elif method == 'mean':
                        self.df[column] = self.df[column].fillna(self.df[column].mean())
                    elif method == 'mode':
                        self.df[column] = self.df[column].fillna(self.df[column].mode()[0])

            except ValueError as ve:
                print(f"Error: {ve}. Please check that you have provided a list of column names formatted as strings.")
            return self.df.copy()

        def impute_nulls_with_median(self, column_list):
            for column in column_list:
                self.df[column] = self.df[column].fillna(self.df[column].median())
            return self.df
        
        def impute_nulls_with_mean(self, column_list):
            for column in column_list:
                self.df[column] = self.df[column].fillna(self.df[column].mean())
            return self.df
        
        def impute_nulls_with_mode(self, column_list):
            for column in column_list:
                self.df[column] = self.df[column].fillna(self.df[column].mode()[0])
            return self.df

        def log_transform(self, column_list):
            for col in column_list:
                self.df[col] = self.df[col].map(lambda i: np.log(i) if i > 0 else 0)
            return self.df
      
        def boxcox_transform(self, column_list):
            for col in column_list:
                boxcox_population, lambda_values = stats.boxcox(self.df[col])
                self.df[col] = boxcox_population
            return self.df
       
        def yeo_johnson_transform(self, column_list):
            for col in column_list:
                nonzero_values = self.df[col][self.df[col] != 0]
                yeojohnson_values, lambda_value = stats.yeojohnson(nonzero_values)
                self.df[col] = self.df[col].apply(lambda x: stats.yeojohnson([x], lmbda=lambda_value)[0] if x != 0 else 0)
            return self.df

            
class StatisticalTests(DataFrameInfo):


    def __init__(self, dataframe):
        self.df = dataframe.copy()

    # TODO I wouldn't call it column_1 and column_list here. Either use independent and dependant variables or use X, y
    # NOTE Really lke the method though 
    def chi_square_test(self, column_1, column_list): # Only between categorical variables
        chi_sq_test_df = self.df.copy()
        chi_sq_test_df[column_1] = chi_sq_test_df[column_1].isnull()
        # Step 2: Crosstab the new column with B
        if len(column_list) > 3:
            for column in column_list:
                contingency_table = pd.crosstab(chi_sq_test_df[column_1], chi_sq_test_df[column])
                # Step 3: Perform chi-squared test
                chi2, p, dof, expected = chi2_contingency(contingency_table)
                if p < 0.05:
                    print(f"Chi-square test for missing values in {column_1} against {column} column: ")
                    print(f"p-value = {p}: Significant")
                    return p
                elif p == 0.05:
                    print(f"Chi-square test for missing values in {column_1} against {column} column: ")
                    print(f"p-value = {p}: Likely not significant")
                    return p
        elif len(column_list) <= 3:
            for column in column_list:
                contingency_table = pd.crosstab(chi_sq_test_df[column_1], chi_sq_test_df[column])
                # Step 3: Perform chi-squared test
                chi2, p, dof, expected = chi2_contingency(contingency_table)
                print(f"Chi-square test for missing values in {column_1} against {column} column: ")
                print(f"p-value = {p}")
                return p
            
    def K2_test(self, column_name): # Test for normality in continuous variables
        stat, p = normaltest(self.df[column_name], nan_policy='omit')
        print('Statistics=%.3f, p=%.3f' % (stat, p))

    # TODO I would move these method below into their own class as they're 
    # related to removng outliers removing outliers. 
    def z_scores(self, column):
        mean_col = np.mean(self.df[column])
        std_col = np.std(self.df[column])
        z_scores = (self.df[column] - mean_col) / std_col
        col_values = self.df[column].copy()
        col_values['z-scores'] = z_scores
        return col_values
    
    # TODO You could use this method inside the method below to get the Q1 and Q3 and get the best of both worlds. 
    def IQR(self, column_list):
        for col in column_list:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            # Calculate IQR
            IQR = Q3 - Q1
            print(f"\nResults for {col} column:")
            print(f"Q1 (25th percentile): {Q1}")
            print(f"Q3 (75th percentile): {Q3}")
            print(f"IQR: {IQR}")
    
    def IQR_outliers(self, column_list):
        for col in column_list:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            # Calculate IQR
            IQR = Q3 - Q1
            print(f"\nResults for {col} column:")
            print(f"Q1 (25th percentile): {Q1}")
            print(f"Q3 (75th percentile): {Q3}")
            print(f"IQR: {IQR}")
            outliers = self.df[(self.df[col] < (Q1 - 1.5 * IQR)) | (self.df[col] > (Q3 + 1.5 * IQR))]
            print("Outliers:")
            print(outliers.shape)


class Plotter(StatisticalTests):


    def __init__(self,dataframe):
        self.df = dataframe.copy()
        
    def discrete_probability_distribution(self, column_name, **kwargs):
        plt.rc("axes.spines", top=False, right=False)
        sns.set_style(style='darkgrid', rc=None)
        probs = self.df[column_name].value_counts(normalize=True)
        # Create bar plot
        dpd = sns.barplot(y=probs.values, x=probs.index)
        dpd.set_xticklabels(dpd.get_xticklabels(), rotation=45, ha='right')
        plt.xlabel('Values')
        plt.ylabel('Probability')
        plt.title('Discrete Probability Distribution')
        plt.show()

    def continuous_probability_distribution(self, column_name, column_list=None):
        if column_list is not None:
            for col in column_list:
                sns.histplot(self.df[col], kde=True, color='blue', stat="probability", bins=30)
                super().print_summary_statistics(col)
        else:
            sns.histplot(self.df[column_name], kde=True, color='blue', stat="probability", bins=30)
            super().print_summary_statistics(column_name)

    def correlation_heatmap(self, column_list):
        sns.heatmap(self.df[column_list].corr(), annot=True, cmap='coolwarm')

    def correlation_matrix_df(self):
        corr = self.df.select_dtypes(include=np.number).corr()
        mask = np.zeros_like(corr, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        # set thins up for plotting
        cmap = sns.diverging_palette(220, 10, as_cmap=True)
        # Draw the heatmap
        sns.heatmap(corr, mask=mask, 
                    square=True, linewidths=.5, annot=True, cmap=cmap)
        plt.yticks(rotation=0)
        plt.title('Correlation Matrix of all Numerical Variables')
        plt.show()

    def qqplot(self,column_list):
        for column in column_list:
            qqplot(self.df[column], scale=1 ,line='q')

    def nulls_dataframe_plot(self):
        msno.matrix(self.df)

    def pair_correlations_grid(self, numeric_features=None):
        if numeric_features is not None:
            sns.pairplot(self.df[numeric_features])
        else:
            numeric_features = super().extract_numeric_features()
            sns.pairplot(self.df[numeric_features])

    def numeric_distributions_grid(self, numeric_features=None, kde=True):
        if numeric_features is not None:
            sns.set(font_scale=0.7)
            f = pd.melt(self.df, value_vars=numeric_features)
            g = sns.FacetGrid(f, col="variable",  col_wrap=3, sharex=False, sharey=False)
            g = g.map(sns.histplot, "value", kde=kde)
        else:
            numeric_features = super().extract_numeric_features()
            sns.set(font_scale=0.7)
            f = pd.melt(self.df, value_vars=numeric_features)
            g = sns.FacetGrid(f, col="variable",  col_wrap=3, sharex=False, sharey=False)
            g = g.map(sns.histplot, "value", kde=kde)

    def count_plot(self, x, **kwargs):
        sns.countplot(x=x)
        x=plt.xticks(rotation=90)

    def count_plots_grid(self, categorical_features):
        # NOTE Try and avoid variables such as g, f, t make it more descriptive
        f = pd.melt(self.df, value_vars=categorical_features)
        g = sns.FacetGrid(f, col='variable',  col_wrap=3, sharex=False, sharey=False)
        g = g.map(self.count_plot, 'value')

    def plot_log_transform(self, col):
        nonzero_values = self.df[col][self.df[col] != 0]
        log_col = nonzero_values.map(lambda i: np.log(i) if i > 0 else 0)
        t=sns.histplot(log_col,label="Skewness: %.2f"%(log_col.skew()), kde=True )
        t.legend()
    
    def plot_boxcox_transform(self, col):
        boxcox_population = self.df[col]
        boxcox_population= stats.boxcox(boxcox_population)
        boxcox_population= pd.Series(boxcox_population[0])
        t=sns.histplot(boxcox_population,label="Skewness: %.2f"%(boxcox_population.skew()) )
        t.legend()
    
    def plot_yeo_johnson_transform(self, col):
        nonzero_values = self.df[col][self.df[col] != 0]
        yeojohnson_population = stats.yeojohnson(nonzero_values)
        yeojohnson_population= pd.Series(yeojohnson_population[0])
        t=sns.histplot(yeojohnson_population,label="Skewness: %.2f"%(yeojohnson_population.skew()) )
        t.legend()
            

    
    


    
    

    

    

        