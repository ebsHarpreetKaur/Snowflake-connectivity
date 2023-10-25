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


# delete_query = "DELETE FROM TRIAL_BALANCE"
# cr.execute(delete_query)



# -------------------------------------------------------------------------------------------------------------------
# STEP : 1

# create_table ='CREATE TABLE TRIAL_BALANCE(POSTING_DATE_MONTHEND_TB DATE)'
# cr.execute(create_table)




# -------------------------------------------------------------------------------------------------------------------
# STEP : 2


# def last_dates_of_months(year):
#     last_dates = []
#     for month in range(1, 13):
#         last_day = calendar.monthrange(year, month)[1]
#         last_date = f"{year}-{month:02d}-{last_day:02d}"
#         last_dates.append(last_date)
#     return last_dates

# specific_year = 2017
# last_dates = last_dates_of_months(specific_year)
# for idx, date in enumerate(last_dates, start=1):
#     sql = "INSERT INTO TRIAL_BALANCE (POSTING_DATE_MONTHEND_TB) VALUES (%s)"
#     values = (date)
#     print(f"Last day of month {idx}: {date}")
#     cr.execute(sql, values)
#     print(values)
    


# -------------------------------------------------------------------------------------------------------------------
# STEP: 3


select_query = '''
SELECT "G/L Account_HKONT","Medical Aid Code.BSEG", BSEG_BUKRS FROM "BSEG View" LIMIT 12
'''

cr.execute(select_query)

rows = cr.fetchall()
print(rows)
print("rows fetched successfully")

# -------------------------------------------------------------------------------------------------------------------
# STEP:4



# table_name = 'TRIAL_BALANCE'
# columns = [
#     'BUKRS_TB VARCHAR',
#     'GL_Account_HKONT_TB VARCHAR',
#     'Medical_Aid_Code_TB VARCHAR'
# ]

# alter_table = f"ALTER TABLE {table_name} ADD COLUMN {', '.join(columns)}"
# cr.execute(alter_table)
# print("table altered")



# -------------------------------------------------------------------------------------------------------------------
# STEP : 5

update_query = """
    UPDATE TRIAL_BALANCE
    SET BUKRS_TB = %s, GL_Account_HKONT_TB = %s, Medical_Aid_Code_TB= %s
"""
for row in rows:
    cr.execute(update_query, (row[0], row[1], row[2]))
    conn.commit()






# insert_query = "UPDATE INTO TRIAL_BALANCE (BUKRS_TB, GL_Account_HKONT_TB, Medical_Aid_Code_TB) VALUES (%s, %s, %s)"

# for row in rows:
#     cr.execute(insert_query, row)
# print("Values updated")










cr.close()
conn.close()










     
     
     
     
     
     
     
     
     	


















