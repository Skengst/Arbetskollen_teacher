#%%
import os
from dotenv import load_dotenv
from snowflake.connector import connect
import pandas as pd


<<<<<<< HEAD:dbt/streamlit_dashboard/connect_data_warehouse.py
#%%
def query_job_listings(query = 'SELECT * FROM mart_job_listings'):
=======
def query_job_listings(query = 'SELECT * FROM mart_job_listings'):
    
>>>>>>> 7411d0faf6bce21e14a2bf25ed604442ab0b6238:streamlit_dashboard/connect_data_warehouse.py
    load_dotenv()

    with connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA'),
        role=os.getenv('SNOWFLAKE_ROLE')

    ) as connection:
        df = pd.read_sql(query, connection)
        return df
    

#%%
print(query_job_listings())    
    


# %%
