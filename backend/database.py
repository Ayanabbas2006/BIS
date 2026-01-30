import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="school_user",
        password="MyPassword#256",
        database="School_DB"
    )
