import snowflake.connector

# Set up connection parameters
params = {
    'user': 'HARPREETKAUR',
    'password': 'Ebullientsoft@1',
    'account': 'rg07701.central-india.azure',
    # 'database': 'FIRST_SNOWFLAKE_DB',
    # 'schema': 'FIRST_SNOWFLAKE_SC'
}
# Establish connection
conn = snowflake.connector.connect(**params)
cr = conn.cursor()

# Create table
cr.execute('CREATE DATABASE TEST_DB')
cr.execute('CREATE SCHEMA TEST_SC')
cr.execute('CREATE TABLE DEVELOPERS(ID NUMBER)')

# sql = "ALTER TABLE EMPLOYEE ADD COLUMN Age VARCHAR(255)"
# Define the SQL statement to add multiple columns
table_name = 'EMPLOYEE'
columns = [
    'MOBILE INT',
    'DESIGNATION VARCHAR',
    'DEPARTMENT VARCHAR'
]

alter_table_sql = f"ALTER TABLE {table_name} ADD COLUMN {', '.join(columns)}"
cr.execute(alter_table_sql)

conn.commit()
cr.close()
conn.close()


