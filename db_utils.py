from sqlalchemy import create_engine, text
import os
import pandas as pd
import yaml


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
    
def save_df_to_csv(df, file_name, destination_folder=None):
    # If a destination folder is provided, create it if it doesn't exist
    if destination_folder:
        os.makedirs(destination_folder, exist_ok=True)
        file_path = os.path.join(destination_folder, file_name)
    else:
        file_path = file_name
        # Save DataFrame to CSV
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")


if __name__ == '__main__':
    my_credentials = load_credentials('credentials.yaml') 
    print(my_credentials)
    database_connector = RDSDatabaseConnector(my_credentials)
    table_name = 'customer_activity'
    customer_activity_df = database_connector.fetch_all_data_to_df(table_name)
    print(type(customer_activity_df))
    print(customer_activity_df.shape)
    csv_file_name = 'customer_activity.csv'
    #save_in_folder = '/Users/silviaaragon/Aicore/exploratory-data-analysis---online-shopping-in-retail'
    save_df_to_csv(customer_activity_df, csv_file_name)




    


