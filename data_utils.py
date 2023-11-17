import pandas as pd


class DataTransform:
        def __init__(self, dataframe):
            self.df = dataframe.copy()
        
        # TODO: add error handling
        # FIXME: astype method syntax
        # TODO: add remaining data types if applicable
        def convert_to_type(self, column_name, data_type):
                try:
                    if data_type == 'datetime':
                        self.df[column_name] = pd.to_datetime(self.df[column_name])
                    elif data_type == 'date':
                        self.df[column_name] = pd.to_datetime(self.df[column_name])
                    elif data_type == 'period':
                        self.df[column_name] = pd.to_timedelta(self.df[column_name])
                    elif data_type == 'categorical':
                        self.df[column_name] = pd.Categorical(self.df[column_name])
                    else:
                        self.df[column_name] = self.df[column_name].astype(data_type)
                except Exception as e:
                    print(f"Error converting column '{column_name}' to type '{data_type}': {e}")
                return self.df.copy()

        def convert_month_to_timedelta(self, column_name):
            try:
                month_map = {'jan': '1M', 'feb': '2M', 'mar': '3M', 'apr': '4M', 'may': '5M', 'jun': '6M',
                            'jul': '7M', 'aug': '8M', 'sep': '9M', 'oct': '10M', 'nov': '11M', 'dec': '12M'}
                self.df[column_name] = self.df[column_name].str.lower().map(month_map).astype('timedelta64')
                return self.df.copy()  # Return a copy of the modified DataFrame
            except Exception as e:
                print(f"Error converting 'month' column to timedelta: {e}")

        def convert_columns(self, column_list, data_type):
            for column in column_list:
                self.convert_to_type(column, data_type)
            return self.df.copy()
    
 
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

    def count_distinct_values(self, columns=None):
        subset = self._get_slice(columns)
        distinct_counts = pd.DataFrame({
            'Column': subset.columns,
            'Distinct Values Count': [subset[column].nunique() for column in subset.columns]
        })
        return distinct_counts

    def print_shape(self, columns=None):
        subset = self._get_slice(columns)
        print("DataFrame Shape:", subset.shape)

    def generate_null_counts(self, columns=None):
        subset = self._get_slice(columns)
        null_counts = subset.isnull().sum()
        null_percentages = (null_counts / len(subset)) * 100
        null_info = pd.DataFrame({
            'Null Count': null_counts,
            'Null Percentage': null_percentages
        })
        return null_info
    

class Plotter:
    pass

        