import boto3
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from utils.helper import create_bucket
from configparser import ConfigParser
from utils.constants import db_tables

config = ConfigParser()
config.read('.env')

region= config['AWS']['region']
bucket_name=config['AWS']['bucket_name']
access_key =config['AWS']['access_key']
secret_key= config['AWS']['secret_key']
host=config['DB_CRED']['host']
username=config['DB_CRED']['username']
password=config['DB_CRED']['password']
database=config['DB_CRED']['database']




bucket_name= 'payminutes'

# Step 1- Create a bucket using boto3
#create_bucket()->commented to avoid running twice




# Extract from Database to Datalake(s3)
db_conn = create_engine(f'postgresql+psycopg2://{username}:{password}@host:5432/{database}')

#df=pd.read_sql_query('SELECT * FROM {table_name}', conn)

s3_path= 's3://{}/{}.csv'



for table in db_tables:
    query= f'SELECT * FROM {table}'
    df=pd.read_sql_query(query,db_conn)
    
    df.to_csv(
        s3_path.format(bucket_name, table)
        , index=False
        , storage_options={
            'key': access_key
            , 'secret': secret_key
        }
    )