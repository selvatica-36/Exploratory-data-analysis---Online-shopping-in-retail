import os
import pandas as pd
import yaml
from sqlalchemy import create_engine, text, exc
from typing import Dict, Optional


def load_credentials(file_path: str) -> Dict:
    """
    Load credentials from a YAML file.

    Parameters:
    - file_path (str): The path to the YAML file containing the credentials.

    Returns:
    - dict: A dictionary containing the loaded credentials.

    Raises:
    - ValueError: If there is an error loading the credentials.

    Example:
    ```
    credentials = load_credentials('path/to/credentials.yml')
    ```
    """
    with open(file_path, 'r') as file:
        try:
            credentials = yaml.safe_load(file)
            if credentials is None:
                raise ValueError("Failed to load credentials. YAML file is empty or malformed.")
            return credentials
        except yaml.YAMLError as e:
            print(f"Error in parsing YAML file: {e}")
    
 
class RDSDatabaseConnector:
    """
    A class for connecting to and interacting with a PostgreSQL database on Amazon's AWS RDS.
    """

    def __init__(self, credentials: Dict) -> None:
        """
        Initialize the RDSDatabaseConnector.

        Parameters:
        - credentials (dict): A dictionary containing the database connection credentials.

        Example:
        ```
        connector = RDSDatabaseConnector(credentials)
        ```
        """
        self.__credentials = credentials
        self.engine = self.__initialise_engine()
        
    def __initialise_engine(self):
        """
        Initialize the SQLAlchemy engine for database connection.

        Returns:
        - sqlalchemy.engine.Engine: The SQLAlchemy engine object.

        Example:
        ```
        engine = connector.initialize_engine()
        ```
        """
        print("***************************")
        print("Attempting to connect to SQL RDS database...")
        db_url =  f"postgresql://{self.__credentials['RDS_USER']}:{self.__credentials['RDS_PASSWORD']}@" \
        + f"{self.__credentials['RDS_HOST']}:{self.__credentials['RDS_PORT']}/" \
        + f"{self.__credentials['RDS_DATABASE']}"
        print("Engine successfully created.")
        return create_engine(db_url)
        
    def connect(self):
        """
        Establish a connection to the database.

        Returns:
        - sqlalchemy.engine.Connection: The database connection object.

        Example:
        ```
        connection = connector.connect()
        ```
        """
        connection = self.engine.connect()
        print("Connected successfully.")
        return connection
    
    def close(self) -> None:
        """
        Close the database connection.

        Example:
        ```
        connector.close()
        ```
        """
        if self.engine:
            self.engine.dispose()
            print("Database connection closed.")
 
    def extract_RDS_to_dataframe(self, table_name: Optional[str] = None, sql_query: Optional[str] = None) -> pd.DataFrame:
        """
        Fetch data from the AWS RDS database and return it as a Pandas DataFrame.

        Parameters:
        - table_name (str, optional): The name of the table to fetch data from.
        - sql_query (str, optional): A custom SQL query to fetch data.

        Returns:
        - pd.DataFrame: The fetched data as a Pandas DataFrame.

        Raises:
        - exc.SQLAlchemyError: If there is an error in the database query.

        Example:
        ```
        df = connector.fetch_data_to_df(table_name='my_table')
        ```
        """
        if sql_query is None and table_name is not None:
            sql_query = f"SELECT * FROM {table_name}"
        elif sql_query is None and table_name is None:
            raise ValueError("Error: Please provide a table_name to extract all data from the table or provide an sql_query.")

        with self.connect() as connection:
            try:
                result = connection.execute(text(sql_query))
                data = result.fetchall()
                columns = result.keys()
                df = pd.DataFrame(data, columns=columns)
                return df
            except exc.SQLAlchemyError as e:
                print(f"Error in executing database query: {e}")
        

def save_df_to_csv(df: pd.DataFrame, file_name: str, destination_folder: Optional[str] = None) -> None:
    """
    Save a Pandas DataFrame to a CSV file.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be saved.
    - file_name (str): The name of the CSV file.
    - destination_folder (str, optional): The folder path where the CSV file will be saved.
    If not provided, the file will be saved in the current working directory.

    Example:
    ```
    save_df_to_csv(my_dataframe, 'output_file.csv', 'output_folder')
    ```
    """
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
    customer_activity_df = database_connector.extract_RDS_to_dataframe(table_name)
    print(type(customer_activity_df))
    print(customer_activity_df.shape)
    csv_file_name = 'customer_activity.csv'
    save_in_folder = 'data'
    save_df_to_csv(customer_activity_df, csv_file_name, save_in_folder)
    help(save_df_to_csv)





    


