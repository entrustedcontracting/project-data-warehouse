"""lorem ipsum."""

# 
import clickhouse_connect, json
# from pyarrow import json
from clickhouse_connect.driver.tools import insert_file
from config import *
from jobSchema import job_schema

# 
client = clickhouse_connect.get_client()
f = open('python-scripts/new_data.json')
  



# 
# client.insert_arrow('company', table)
# insert_file(client, 'company', 'python-scripts/MOCK_DATA.csv')

# 
# results = client.query('select * from company limit 10')
# print(results.result_rows)
# 
 





