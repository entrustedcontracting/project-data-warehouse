"""lorem ipsum."""

# 
import clickhouse_connect, json, csv, polars as pl
from config import *

# 
client = clickhouse_connect.get_client(database='entrustedData')
df = pl.read_csv(source='python-scripts/MOCK_DATA.csv')
# print(df.schema)

# 
client.command(
    cmd="""
    create table if not exists test 
        (
            id Int32,
            name String,
            age UInt8
        )
    Engine = MergeTree()
    order by id
    """
)
client.command('SET input_format_skip_unknown_fields=1')

# 
print(client.command("describe table entrustedData.test"))
data = [
    {'id': 1, 'name': 'John', 'age': 25},
    {'id': 2, 'name': 'Alice', 'age': 30},
    {'id': 3, 'name': 'Bob', 'age': 35}
]

# 


results = client.query('select * from test')
print(results)
# 
 





