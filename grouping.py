import snowflake.connector

# Set up connection parameters
SNOWFLAKE_ACCOUNT = "fd76372.eu-west-1"
SNOWFLAKE_USER = "HARPREET"
SNOWFLAKE_PASSWORD = "HarpreetLenmed1"
SNOWFLAKE_DATABASE = "APPLICATION_DB"
SNOWFLAKE_SCHEMA = "MAIN"
SNOWFLAKE_WAREHOUSE = "APP_VWH"
SNOWFLAKE_AUTOCOMMIT = True

params = {
    'user': SNOWFLAKE_USER,
    'password': SNOWFLAKE_PASSWORD,
    'account': SNOWFLAKE_ACCOUNT,
    'warehouse': SNOWFLAKE_WAREHOUSE,
    'database': SNOWFLAKE_DATABASE,
    'schema': SNOWFLAKE_SCHEMA,
    'autocommit': SNOWFLAKE_AUTOCOMMIT
}
# connection
conn = snowflake.connector.connect(**params)
cr = conn.cursor()

table_name = 'TRIAL_BALANCE'
columns = [
    'BUKRS VARCHAR',
    'HKONT INT',
    'Medical_Aid VARCHAR'
]
alter_table_sql = f"ALTER TABLE {table_name} ADD COLUMN {', '.join(columns)}"

insert_query = '''
INSERT INTO TRIAL_BALANCE (HKONT, Medical_Aid)
SELECT "G/L Account_HKONT", "Medical Aid Code.BSEG"
FROM "BSEG View"
'''
table_name = "BSEG View"
query = f'SELECT * FROM {table_name} LIMIT 10'

cr.execute(query)

# Fetch all rows from the result set
rows = cr.fetchall()

# Access individual columns using index or column names:
# for row in rows:
#     # Access individual columns using row[index]
#     Age = row[0]
#     Salary = row[1]
#     # Process the values as required
#     print(Age, Salary)

# print(rows)
print('rows-------------------------------------------', rows)

conn.commit()
cr.close()
conn.close()










     
     
     
     
     
     
     
     
     	


















