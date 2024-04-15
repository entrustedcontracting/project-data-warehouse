"""lorem ipsum."""

# 
import clickhouse_connect, json, csv, polars as pl
from config import *

# 
client = clickhouse_connect.get_client(database='entrustedData')
df = pl.read_csv(source='python-scripts/MOCK_DATA.csv')
print(df.schema)

# 
# client.command(
#     cmd="""
#     create table company 
#         (
#             company_id String, 
#             name String,
#             website Nullable(String),
#             linkedin_url Nullable(String),
#             inferred_employee_count Nullable(Int64),
#             industry String,
#             city String,
#             state String,
#             zip_code Nullable(String),
#             street_address Nullable(String),
#             founded Nullable(Int64),
#             is_referral_source Boolean
#         )
#     Engine MergeTree()
#     order by company_id
#     """
# )

# 
print(client.command("describe table entrustedData.company"))

# 
client.insert(
    table='company', 
    database='entrustedData', 
    data=['43f9c3b-5972-4921-b60a-bf8ce64d4cd1','shufflebeat','netvibes.com','squarespace.com/in/sapien/iaculis/congue/vivamus.aspx',328,'construction/ag equipment/trucks','miami','florida','33169','6 golf course street',1995,True])
results = client.query('select * from company limit 10')
print(results)
# 
 





