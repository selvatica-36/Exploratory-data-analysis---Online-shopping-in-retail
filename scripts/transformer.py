from scipy import stats
from typing import List
import numpy as np
import pandas as pd


class DataTransform:
    """
    A class for performing various transformations on a DataFrame.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame to transform.

    Example:
    ```
    transformer = DataTransform(my_dataframe)
    ```

    """    
    def __init__(self, dataframe: pd.DataFrame):
        """
        Initialize the DataTransform object with a DataFrame. Used internally when an instance of the call is called.

        Parameters:
        - dataframe (pd.DataFrame): The DataFrame to transform.

        """
        self.df = dataframe.copy()
    
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
        df = transformer.impute_nulls(['column1', 'column2'], 'mean')
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

    def impute_nulls_with_median(self, column_list: List[str]) -> pd.DataFrame:
        """
        Impute null values in specified columns using the median.

        Parameters:
        - column_list (List[str]): List of column names to impute null values.

        Returns:
        - pd.DataFrame: A copy of the DataFrame with null values imputed.

        Example:
        ```
        df = transformer.impute_nulls_with_median(['column1', 'column2'])
        ```

        """
        for column in column_list:
            self.df[column] = self.df[column].fillna(self.df[column].median())
        return self.df
    
    def impute_nulls_with_mean(self, column_list: List[str]) -> pd.DataFrame:
        """
        Impute null values in specified columns using the mean.

        Parameters:
        - column_list (List[str]): List of column names to impute null values.

        Returns:
        - pd.DataFrame: A copy of the DataFrame with null values imputed.

        Example:
        ```
        df = transformer.impute_nulls_with_mean(['column1', 'column2'])
        ```

        """
        for column in column_list:
            self.df[column] = self.df[column].fillna(self.df[column].mean())
        return self.df
    
    def impute_nulls_with_mode(self, column_list: List[str]) -> pd.DataFrame:
        """
        Impute null values in specified columns using the mode.

        Parameters:
        - column_list (List[str]): List of column names to impute null values.

        Returns:
        - pd.DataFrame: A copy of the DataFrame with null values imputed.

        Example:
        ```
        df = transformer.impute_nulls_with_mode(['column1', 'column2'])
        ```

        """
        for column in column_list:
            self.df[column] = self.df[column].fillna(self.df[column].mode()[0])
        return self.df
    
    def impute_nulls_with_zeros(self, column_list):
        """
        Impute null values in specified columns with zeros.

        Parameters:
        - column_list (List[str]): List of column names to impute null values.

        Returns:
        - pd.DataFrame: A copy of the DataFrame with null values imputed.

        Example:
        ```
        df = transformer.impute_nulls_with_zeros(['column1', 'column2'])
        ```

        """
        for col in column_list:
            self.df[col] = self.df[col].fillna(0)

    def log_transform(self, column_list: List[str]) -> pd.DataFrame:
        """
        Apply a log transformation to specified columns.

        Parameters:
        - column_list (List[str]): List of column names to transform.

        Returns:
        - pd.DataFrame: Transformed DataFrame.

        Example:
        ```
        transformed_df = transformer.log_transform(['column1', 'column2'])
        ```

        """
        for col in column_list:
            self.df[col] = self.df[col].map(lambda i: np.log(i) if i > 0 else 0)
        return self.df
    
    def boxcox_transform(self, column_list: List[str]) -> pd.DataFrame:
        """
        Apply a Box-Cox transformation to specified columns.

        Parameters:
        - column_list (List[str]): List of column names to transform.

        Returns:
        - pd.DataFrame: Transformed DataFrame.

        Example:
        ```
        transformed_df = transformer.boxcox_transform(['column1', 'column2'])
        ```

        """
        for col in column_list:
            boxcox_population, lambda_values = stats.boxcox(self.df[col])
            self.df[col] = boxcox_population
        return self.df
    
    def yeo_johnson_transform(self, column_list: List[str]) -> pd.DataFrame:
        """
        Apply a Yeo-Johnson transformation to specified columns.

        Parameters:
        - column_list (List[str]): List of column names to transform.

        Returns:
        - pd.DataFrame: Transformed DataFrame.

        Example:
        ```
        transformed_df = transformer.yeo_johnson_transform(['column1', 'column2'])
        ```

        """
        for col in column_list:
            nonzero_values = self.df[col][self.df[col] != 0]
            yeojohnson_values, lambda_value = stats.yeojohnson(nonzero_values)
            self.df[col] = self.df[col].apply(lambda x: stats.yeojohnson([x], lmbda=lambda_value)[0] if x != 0 else 0)
        return self.df
    
