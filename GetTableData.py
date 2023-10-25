import snowflake.connector

# Set up connection parameters
params = {
    'user': 'HARPREETKAUR',
    'password': 'Ebullientsoft@1',
    'account': 'rg07701.central-india.azure',
    'database': 'FIRST_SNOWFLAKE_DB',
    'schema': 'FIRST_SNOWFLAKE_SC'
}
# Establish connection
conn = snowflake.connector.connect(**params)
cr = conn.cursor()

table_name = 'EMPLOYEE'
query = f'SELECT * FROM {table_name}'

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

print(rows)

conn.commit()
cr.close()
conn.close()


