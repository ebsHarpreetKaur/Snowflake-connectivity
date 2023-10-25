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
# query = f'SELECT * FROM "Calendar View" LIMIT 5'

create_table ='CREATE TABLE TRIAL_BALANCE(Posting_Date_MonthEnd VARCHAR(50), Company_Code_BUKRS_BSEG VARCHAR(300), G_L_Account_HKONT VARCHAR(200), Medical_Aid_Code_BSEG VARCHAR(200))'
insert_query = '''
INSERT INTO TRIAL_BALANCE (Posting_Date_MonthEnd)
SELECT MY_DATE
FROM "Calendar View"
WHERE YEAR >= '2017';
'''

get_query = '''
SELECT DISTINCT
    CONCAT(BUKRS, '.', BSEG) AS Company_Code_BUKRS_BSEG,
    HKONT AS G_L_Account_HKONT,
    `Medical Aid Code.BSEG` AS Medical_Aid_Code_BSEG
FROM
    `TRIAL_BALANCE`
JOIN
    BSEG ON `TRIAL_BALANCE`.BSEG = BSEG
LIMIT 10'''

# cr.execute(create_table)
# cr.execute(insert_query)
cr.execute(get_query)

rows = cr.fetchall()
print('rows-------------------------------------------', rows)

conn.commit()
cr.close()
conn.close()










     
     
     
     
     
     
     
     
     	


















