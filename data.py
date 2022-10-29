import psycopg2

try:
    connect = psycopg2.connect(
        database="users",
        user="",
        password="",
        host="127.0.0.1",
        port="2000",
    )

    with connect.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE users(
            id SERIAL PRIMARY KEY NOT NULL IDENTITY(1,1)
            first_name varchar(50) NOT NULL
            second_name varchar(50) NOT NULL
            number_phone integer NOT NULL,
            job_title varchar(50) NOT NULL,
            username varchar(50) NOT NULL UNIQUE,
            password varhar(50) NOT NULL,
            role bool,NOT NULL
            
            )
            """
        )
except Exception as ex:
    print("Error PosthreSQL")
finally:
    if connect:
        connect.close()
