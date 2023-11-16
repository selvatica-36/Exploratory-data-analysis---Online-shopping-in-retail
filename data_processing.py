import pandas as pd


class DataTransform:
    def __init__(self,df):
        self.df = df.copy()

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
            else:
                print(f"Unsupported data type: {data_type}")
        except Exception as e:
            print(f"Error converting column '{column_name}' to type '{data_type}': {e}")

    def convert_columns(self, column_list, data_type):
        for column in column_list:
            self.convert_to_type(column, data_type)

    def get_dataframe(self):
        return self.df
        