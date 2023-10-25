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

create_table_query ='CREATE TABLE Trial_Balance(ID INT, SELECTED_DATE VARCHAR(50), SELECTED_MONTH VARCHAR(50))'
insert_query = '''
INSERT INTO Trial_Balance (ID, selected_date, selected_month)
SELECT DAY_OF_MON,MY_DATE, MONTH_NAME
FROM "Calendar View"
WHERE MY_DATE >= '2017-01-01';
'''
# query = f'SELECT * FROM "Calendar View" LIMIT 5'
cr.execute(create_table_query)
cr.execute(insert_query)
# Fetch all rows from the result set
# rows = cr.fetchall()

# Access individual columns using index or column names:
# for row in rows:
#     # Access individual columns using row[index]
#     row1 = row[1]
#     row2 = row[3]
#     # Process the values as required
#     print(row1, row2)

# print(rows)


conn.commit()
cr.close()
conn.close()

# query = f"CREATE VIEW it_employees AS SELECT MANDT FROM LENMED_BSEG WHERE BUKRS = '3030' LIMIT 10"
























































