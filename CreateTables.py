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

conn.commit()
cr.close()
conn.close()


