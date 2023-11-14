import pandas as pd
import yaml
from sqlalchemy import create_engine, text


def load_credentials(file_path):
    with open(file_path, 'r') as file:
        try:
            credentials = yaml.safe_load(file)
            return credentials
        except yaml.YAMLError as e:
            print(f"Error in parsing YAML file: {e}")
    
 
class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = self.initialise_engine()
    def initialise_engine(self):
        db_url = f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        return create_engine(db_url)
    def connect(self):
        return self.engine.connect()
    def close(self):
        if self.engine:
            self.engine.dispose()
            print("Database connection closed.")
    def fetch_all_data_to_df(self, table_name):
        sql_query = text(f"SELECT * FROM {table_name}")
        with self.connect() as connection:
            result = connection.execute(sql_query)
            data = result.fetchall()  # Fetch all rows from the result set
            columns = result.keys()   # Get column names
            df = pd.DataFrame(data, columns=columns)
            return df
    def execute_query_to_df(self, sql_query):
        with self.connect() as connection:
            result = connection.execute(text(sql_query))
            data = result.fetchall()  # Fetch all rows from the result set
            columns = result.keys()   # Get column names
            df = pd.DataFrame(data, columns=columns)
            return df
    

if __name__ == '__main__':
    my_credentials = load_credentials('credentials.yaml') 
    print(my_credentials)
    database_connector = RDSDatabaseConnector(my_credentials)
    table_name = 'customer_activity'
    customer_activity_df = database_connector.fetch_all_data_to_df(table_name)
    print(type(customer_activity_df))
    

    


