from sqlalchemy import create_engine, text
import os
import pandas as pd
import yaml
# TODO I would doc string your methods it will elevate the standard of your code and make it more
# maintainable and readable in the future and for employers viewing the code. 
# TODO I would add typing to each of the parameters in your methods
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
        db_url =  f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@" \
        + f"{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/" \
        + f"{self.credentials['RDS_DATABASE']}"
        return create_engine(db_url)
        
    def connect(self):
        return self.engine.connect()
    
    def close(self):
        if self.engine:
            self.engine.dispose()
            print("Database connection closed.")
 
    def fetch_data_to_df(self, table_name = None, sql_query = None):
        if sql_query == None & table_name != None:
            sql_query = f"SELECT * FROM {table_name}" # If no query provided, selects all data from table
        elif sql_query == None & table_name == None:
            print("Error: Please, provide a table_name to extract all data from the table or provide a custom sql_query.")

        # Use context manager to open connection, extract data and close the connection.
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
    save_in_folder = 'data'
    save_df_to_csv(customer_activity_df, csv_file_name, save_in_folder)




    


