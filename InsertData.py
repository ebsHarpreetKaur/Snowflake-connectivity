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

sql = "INSERT INTO EMPLOYEE (ID, Name, Age, Mobile, Designation, Department) VALUES (%s, %s, %s, %s, %s, %s)"
values = ('2', 'Ella', '27', '3425636564', 'Developer', 'IT')
cr.execute(sql, values)

conn.commit()
cr.close()
conn.close()


