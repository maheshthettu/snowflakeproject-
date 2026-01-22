import snowflake.connector as sf

def snowflake_connection_user_password(**kwargs):
    
    print("-------------------Snowflake Connection -------------------")
    print("starting connection to snowflake")

    conn = sf.connect(**kwargs)
    print("connceted to snowflake!")
    print("Returning Connection")
    print("-------------------------------------------------------")
    return conn

