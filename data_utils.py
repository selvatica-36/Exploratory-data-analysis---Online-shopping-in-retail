import pandas as pd
import numpy as np

class DataTransform:
        def __init__(self, dataframe):
            self.df = dataframe.copy()
        
        # TODO: add error handling
        # TODO: add remaining data types if applicable
        def convert_to_type(self, column_name, data_type, ignore_errors = True):
                data_type = data_type.lower()
                if ignore_errors == True:
                    try:
                        if data_type == 'datetime':
                            self.df[column_name] = pd.to_datetime(self.df[column_name], errors = 'coerce')
                        elif data_type == 'date':
                            self.df[column_name] = pd.to_datetime(self.df[column_name], errors = 'coerce')
                        elif data_type == 'categorical':
                            self.df[column_name] = pd.Categorical(self.df[column_name])
                        elif data_type == 'str':
                            self.df[column_name] = self.df[column_name].astype(str, errors='ignore')
                        elif data_type == 'float' or data_type == 'float64':
                            self.df[column_name] = self.df[column_name].astype(float, errors='ignore')
                        elif data_type == 'int' or data_type == 'int64':
                            self.df[column_name] = self.df[column_name].astype(int, errors='ignore')
                        elif data_type == 'bool':
                            self.df[column_name] = self.df[column_name].astype(bool, errors='ignore')
                        else:
                            print(f"Error: data type {data_type} not supported. Check docstrings or call help for more information.")
                    except Exception as e:
                        print(f"Error converting column '{column_name}' to type '{data_type}': {e}")
                    return self.df.copy()
                elif ignore_errors == False:
                    try:
                        if data_type == 'datetime':
                            self.df[column_name] = pd.to_datetime(self.df[column_name])
                        elif data_type == 'date':
                            self.df[column_name] = pd.to_datetime(self.df[column_name])
                        elif data_type == 'timedelta':
                            self.df[column_name] = pd.to_timedelta(self.df[column_name])
                        elif data_type == 'categorical':
                            self.df[column_name] = pd.Categorical(self.df[column_name])
                        elif data_type == 'str':
                            self.df[column_name] = self.df[column_name].astype(str)
                        elif data_type == 'float' or data_type == 'float64':
                            self.df[column_name] = self.df[column_name].astype(float)
                        elif data_type == 'int' or data_type == 'int64':
                            self.df[column_name] = self.df[column_name].astype(int)
                        elif data_type == 'bool':
                            self.df[column_name] = self.df[column_name].astype(bool)
                        else:
                            print(f"Error converting column '{column_name}' to type '{data_type}': {e}")
                    except Exception as e:
                        print(f"Error converting column '{column_name}' to type '{data_type}': {e}")
                    return self.df.copy()
                else:
                    print("Error: the parameter 'ignore_errors' is a bool and can only be True or False.")


        def convert_month_to_period(self, column_name):
            try:
                self.df[column_name] = self.df[column_name].astype(str)
                self.df['month'] = self.df['month'].str.lower()
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
        
        def impute_nulls(self):
            pass

    
 
 # TODO: add error handling
class DataFrameInfo:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def _get_slice(self, columns=None):
        if columns is not None:
            try:
                if isinstance(columns, list): # slice by column names
                    columns = [col.lower() for col in columns]
                    return self.df[columns]
                elif isinstance(columns, str): #choose one column only, allows for string outside list
                    columns = columns.lower()
                    return self.df[[columns]]
                elif isinstance(columns, tuple) and len(columns) == 2 and all(isinstance(col, int) for col in columns):
                    return self.df.iloc[:, columns[0]:columns[1] + 1]
                else:
                    raise ValueError
            except KeyError as ke:
                print(f"KeyError: you need to provide a valid column name: {ke}")
            except ValueError as ve:
                print(f"ERROR: Invalid columns parameter. Use a list of valid column names formatted as strings, or a numerical interval formatted as a tuple e.g. (0,3): {ve}")
            except AttributeError as ae:
                print(f"ERROR: Invalid columns parameter. Use a list of valid column names formatted as strings, or a numerical interval formatted as a tuple e.g. (0,3): {ae}")
        else:
            return self.df
    def extract_column_names(self, columns=None):
        subset = self._get_slice(columns)
        return list(subset.columns)
    def data_types_columns(self, columns=None):
        subset = self._get_slice(columns)
        return subset.dtypes
    def info_columns(self, columns=None):
        subset = self._get_slice(columns)
        return subset.info()
    def extract_statistical_values(self, columns=None):
        subset = self._get_slice(columns)
        return subset.describe()
    def show_distinct_values(self,columns=None):
        subset = self._get_slice(columns)
        for column in subset:
            try:
                print(f"Unique values in {column}:", np.sort(self.df[column].unique()))
            except TypeError:
                print(f"Unique values in {column}:", self.df[column].unique())
    def count_distinct_values(self, columns=None):
        subset = self._get_slice(columns)
        distinct_counts = pd.DataFrame({
            'column': subset.columns,
            'distinct_values_count': [subset[column].nunique() for column in subset.columns]
        })
        distinct_counts.set_index(['column'], inplace=True)
        return distinct_counts
    def print_shape(self, columns=None):
        subset = self._get_slice(columns)
        print("DataFrame Shape:", subset.shape)
    def generate_null_counts(self, columns=None):
        subset = self._get_slice(columns)
        null_counts = subset.isnull().sum()
        null_percentages = (null_counts / len(subset)) * 100
        null_info = pd.DataFrame({
            'null_count': null_counts,
            'null_percentage': null_percentages
        })
        return null_info



class Plotter:
    def __init__(self,dataframe):
        self.df = dataframe.copy()
    def discrete_probability_distribution(self, column_name):
        plt.rc("axes.spines", top=False, right=False)
        sns.set_style(style='darkgrid', rc=None)
        style.use('fivethirtyeight')
        five_thirty_eight = [
            "#30a2da",
            "#fc4f30",
            "#e5ae38",
            "#6d904f",
            "#8b8b8b",
        ]
        sns.set_palette(five_thirty_eight)
        probs = self.df[column_name].value_counts(normalize=True)
        # Create bar plot
        dpd = sns.barplot(y=probs.values, x=probs.index,palette=five_thirty_eight)
        plt.xlabel('Values')
        plt.ylabel('Probability')
        plt.title('Discrete Probability Distribution')
        plt.show()
        print(f"The mode of the distribution is {self.df[column_name].mode()[0]}")
        print(f"The mean of the distribution is {self.df[column_name].mean()}")
        print(f"The median of the distribution is {self.df[column_name].median()}")

    def correlation_heatmap(self, column_list):
        sns.heatmap(self.df[column_list].corr(), annot=True, cmap='coolwarm')

    

    

    

        