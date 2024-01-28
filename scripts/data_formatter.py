from typing import List
import numpy as np
import pandas as pd


class DataFormat:
    """
    A class for performing various operations related to data formatting on a DataFrame.
    """
    def __init__(self, dataframe: pd.DataFrame):
        
        self.df = dataframe.copy()

    def convert_to_type(self, column_name: str, data_type: str, ignore_errors: bool = True) -> pd.DataFrame:
        """
        Convert a specific column in the DataFrame to the specified data type.

        Parameters:
        - column_name (str): Name of the column to be converted.
        - data_type (str): Target data type.
        - ignore_errors (bool, optional): Whether to ignore errors during conversion. Default is True.

        """
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

    def convert_month_to_period(self, column_name: str) -> pd.DataFrame:
        """
        Convert a column representing months to a period format.

        Parameters:
        - column_name (str): Name of the column to be converted.

        Returns:
        - pd.DataFrame: A copy of the DataFrame with the converted column.

        """
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
    
    def convert_columns(self, column_list: List[str], data_type: str, ignore_errors: bool = True) -> pd.DataFrame:
        """
        Convert multiple columns to the specified data type.

        Parameters:
        - column_list (List[str]): List of column names to be converted.
        - data_type (str): Target data type.
        - ignore_errors (bool, optional): Whether to ignore errors during conversion. Default is True.

        Returns:
        - pd.DataFrame: A copy of the DataFrame with the converted columns.

        """
        for column in column_list:
            self.convert_to_type(column, data_type, ignore_errors)
        return self.df.copy()
    
    def strings_to_dates(self, column_list: List[str]) -> pd.DataFrame:
        """
        Convert columns containing string representations of dates to datetime objects.

        Parameters:
        - column_list (List[str]): List of column names containing string representations of dates.

        Returns:
        - pd.DataFrame: A copy of the DataFrame with the converted columns.

        """
        for col in column_list:
            self.df[col] = pd.to_datetime(self.df[col], format="%b-%Y")
        return self.df.copy()
        
    def rename_column(self, col_name: str, new_col_name: str) -> pd.DataFrame:
        """
        Rename a column in the DataFrame.

        Parameters:
        - col_name (str): Current name of the column.
        - new_col_name (str): New name for the column.

        Returns:
        - pd.DataFrame: A copy of the DataFrame with the renamed column.

        """
        self.df.rename(columns={col_name: new_col_name}, inplace=True)
        return self.df.copy()

    def round_float(self, column: str, decimal_places: int) -> pd.DataFrame:
        """
        Round the values in a column to a specified number of decimal places.

        Parameters:
        - column (str): Name of the column to be rounded.
        - decimal_places (int): Number of decimal places to round to.

        Returns:
        - pd.DataFrame: A copy of the DataFrame with the rounded column.

        """
        self.df[column] = self.df[column].apply(lambda x: round(x, decimal_places))
        return self.df.copy()

    def extract_num_from_string(self, columns: List[str]) -> pd.DataFrame:
        """
        Extract numerical values from string representations in specified columns.

        Parameters:
        - columns (List[str]): List of column names to be processed.

        Returns:
        - pd.DataFrame: A copy of the DataFrame with the extracted values.

        """
        for col in columns:
            self.df[col] = self.df[col].str.extract('(\d+)', expand=False)
        return self.df.copy()