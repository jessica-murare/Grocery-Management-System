import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(
            user='root',
            password='Ky@12345',
            host='localhost',
            database='grocery_store'
        )
    return __cnx
