import pandas as pd


class DataTransform:
        def __init__(self, dataframe):
            self.df = dataframe.copy()
            
        def convert_to_type(self, column_name, data_type):
                try:
                    if data_type == 'str':
                        self.df[column_name] = self.df[column_name].astype(str)
                    elif data_type == 'timestamp':
                        self.df[column_name] = pd.to_datetime(self.df[column_name])
                    elif data_type == 'float':
                        self.df[column_name] = self.df[column_name].astype(float)
                    elif data_type == 'int':
                        self.df[column_name] = self.df[column_name].astype(int)
                    elif data_type == 'object':
                        self.df[column_name] = self.df[column_name].astype(object)
                    elif data_type == 'category':
                        self.df[column_name] = self.df[column_name].astype('category') #??
                    #elif data_type == '':
                        #self.df[column_name] = self.df[column_name].astype()
                    else:
                        print(f"Unsupported data type: {data_type}")
                except Exception as e:
                    print(f"Error converting column '{column_name}' to type '{data_type}': {e}")

        def convert_columns(self, column_list, data_type):
            for column in column_list:
                self.convert_to_type(column, data_type)

        def get_dataframe(self):
            return self.df
        

class DataFrameInfo:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def _get_slice(self, columns):
        if columns is not None:
            return self.df[columns]
        return self.df

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
        distinct_counts = {}
        for column in subset.columns:
            distinct_counts[column] = subset[column].nunique()
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

        