import mysql.connector
from mysql.connector import Error

_connection = None


def connectDB():
    global _connection
    _connection  = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
    print("DB Connected")


def createDB():
    print('DB Creation')
    db_cursor = _connection.cursor()
    try:
        dbname  = raw_input("Enter DB Name :::::: \t")
        db_cursor.execute("CREATE DATABASE "+dbname)
    except Error as exception:
        print('Unable to create DB',exception)


def main():
    connectDB()
    print("1. Create DB \n 2. DROP DB")
    print("---------------------------")

    opr = input("Enter Input ::::: \t")
    print("---------------------------")

    if opr == 1:
        createDB()



if __name__ == "__main__":
        main()
