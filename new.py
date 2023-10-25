import snowflake.connector
import calendar

# Set up connection parameters
SNOWFLAKE_ACCOUNT = "fd76372.eu-west-1"
SNOWFLAKE_USER = "HARPREET"
SNOWFLAKE_PASSWORD = "Harpreet123"
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

# -------------------------------------------------------------------------------------------------------------------

# create_table ='CREATE TABLE TRIAL_BALANCE(POSTING_DATE_MONTHEND DATE)'
# cr.execute(create_table)
# print(f"Table created successfully")

# -------------------------------------------------------------------------------------------------------------------

def last_dates_of_months(year):
    last_dates = []
    for month in range(1, 13):
        last_day = calendar.monthrange(year, month)[1]
        last_date = f"{year}-{month:02d}-{last_day:02d}"
        last_dates.append(last_date)
    return last_dates

specific_year = 2017
last_dates = last_dates_of_months(specific_year)
for idx, date in enumerate(last_dates, start=1):
    sql = "INSERT INTO TRIAL_BALANCE (POSTING_DATE_MONTHEND) VALUES (%s)"
    values = (date)
    print(f"Last day of month {idx}: {date}")
    cr.execute(sql, values)
    

# def last_dates_of_months(year):
#     last_dates = []
#     for month in range(1, 13):
#         last_day = calendar.monthrange(year, month)[1]
#         last_date = f"{year}-{month:02d}-{last_day:02d}"
#         last_dates.append(last_date)
#     return last_dates

# specific_year = 2017
# last_dates = last_dates_of_months(specific_year)
# print(last_dates)
# insert_query = "INSERT INTO TRIAL_BALANCE (POSTING_DATE_MONTHEND) VALUES (%s)"
# try:
#     cr.executemany(insert_query, [(date,) for date in last_dates])
#     conn.commit()
#     print("Last dates inserted into Snowflake successfully!")
# except snowflake.connector.errors.DatabaseError as e:
#     print("Error:", e)
# -------------------------------------------------------------------------------------------------------------------





# delete_query = f"DELETE FROM TRIAL_BALANCE"
# cr.execute(delete_query)


conn.commit()
cr.close()
conn.close()










     
     
     
     
     
     
     
     
     	


















