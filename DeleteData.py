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

# Execute the DELETE statement
delete_query = "DELETE FROM EMPLOYEE WHERE ID = NULL"
cr.execute(delete_query)

conn.commit()
cr.close()
conn.close()



