from  snowflake_connection import snowflake_connection_user_password as up
import pandas as pd

connection = up(
    user="MAHESH",
    password="Mahee@8374138092",
    account="SROTSLD-VP20091"
)
cur=connection.cursor()
cur.execute("SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_DATABASE()")
df = cur.fetch_pandas_all()
print(df.head())



