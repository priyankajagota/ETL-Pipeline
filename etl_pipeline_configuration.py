# IMPORT LIBRARIES
from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL


from dotenv import dotenv_values

config = dotenv_values(".env")

load_dotenv()

# GET PASSWORD FROM ENVIRONMENT VARIABLES

uid = os.getenv("user")
pwd= os.getenv('password')



driver = "{ODBC Driver 17 for SQL Server}"
server = "localhost"
database = "AdventureWorks2019"

#connect to sql server database and extract data from sql server



#extract data from sql server
def extract():
    try:
        connection_string = 'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd + ';TRUSTED_CONNECTION=' + "YES"
        connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
        src_engine = create_engine(connection_url)
        src_conn = src_engine.connect()
        # execute query
        query = """ SELECT * FROM sys.Tables """
        src_tables_df = pd.read_sql_query(query, src_conn)
        src_tables = src_tables_df['name'].to_dict()
        print(src_tables_df)
        

        for id in src_tables:
            table_name = src_tables[id]
            query1 = f"select TABLE_SCHEMA from INFORMATION_SCHEMA.TABLES where TABLE_NAME = '{table_name}'"
            schema_name = pd.read_sql_query(query1, src_conn)
            val = schema_name.loc[0]['TABLE_SCHEMA']
          
            query2= f'select * FROM {val}.{table_name}'
            df = pd.read_sql_query(query2, src_conn)
            
            load(df, table_name)
        

    except Exception as e:
        print("Data extract error: " + str(e))
#load data to postgres
def load(df, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:5432/etlprocess')
        print(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
        # save df to postgres
        df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False, chunksize=100000)
        rows_imported += len(df)
        # add elapsed time to final print out
        print("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))
        
        
try:
    #call extract function
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))
