import psycopg2

try:
    connection = psycopg2.connect(user = "uddryrqqwkwlsc",
                                  password = "3b98b22e12c3a62ca65e7dde7d8d8997d3c2bcea1f7eece8ecd8fd3e0847e7ad",
                                  host = "ec2-54-225-113-7.compute-1.amazonaws.com",
                                  port = "5432",
                                  database = "dct2ve2tgdnrc2")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")