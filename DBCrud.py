import mysql.connector
import requests
from mysql.connector import Error

_connection = None


def connectDB():
    global _connection
    _connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="test"
    )

def closeConnection():
    if _connection is not None and _connection.is_connected:
        _connection.close
        print('Disconnected from database')

def dbList():
    mycursor = _connection.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

def dbCreate():
    try:
        mycursor = _connection.cursor()
        dbname = raw_input('Enter DB Name  ::: \t')
        mycursor.execute("CREATE DATABASE "+ dbname)
    except Error as e:
        print("\nDB create exception ::: ", e)

def dropDB():
    try:
        mycursor = _connection.cursor()
        dbname = raw_input('Enter DB Name  ::: \t')
        mycursor.execute("DROP DATABASE "+ dbname)
    except Error as e:
        print("\nDB create exception ::: ", e)

def createTable():
    try:
        mycursor = _connection.cursor()
        mycursor.execute("CREATE TABLE student (rollno VARCHAR(255), name VARCHAR(255), address VARCHAR(500) )")
        mycursor.execute("SHOW TABLES")
        print("Tables List")
        for x in mycursor:
            print(x)

    except Error as e:
        # mycursor.execute("DROP TABLE student")
        # mycursor.execute("CREATE TABLE student (rollno VARCHAR(255), name VARCHAR(255), address VARCHAR(500) )")
        # print('Table Dropped  & created')
        print("\nTable create exception ::: ", e)

def create():
    print("Record  Operation")
    db_cursor = _connection.cursor()
    try:
        sql = "INSERT INTO student (rollno, name, address) VALUES (%s, %s, %s)"
        val = [
            ('1001','Ram','madurai'),
            ('1002','kumar','Chennai'),
            ('1003', 'Alan', 'NewYork'),
            ('1004', 'Krish', 'Delhi'),
            ('1005', 'Suman', 'Kolkata')
        ]
        db_cursor.executemany(sql, val)
        _connection.commit()
        print(db_cursor.rowcount, "rows was inserted.")
        1
    except Error as e:
        print('unable to insert ',e)

def read():
    print("Read Operation")
    db_cursor = _connection.cursor()
    sql_select_query = "select * from student"
    try:
        db_cursor.execute(sql_select_query)
        records = db_cursor.fetchall()
        print("\nPrinting each student record")
        for row in records:
            print (row)
            # print('Roll No  - ',str(row[0]))
            # print('Name  - ',row[1])
            # print('Address  - ',row[2])

    except Error as e:
        print ('Error while fetching record', e)

def update():
    print("Update Operation")
    db_cursor = _connection.cursor()
    sql_update_query = "UPDATE student SET name = 'ajay' where rollno ='1002'"
    try:
        db_cursor.execute(sql_update_query)
        _connection.commit()
        print(db_cursor.rowcount, "rows was inserted.")
        read()
    except Error as e:
        print('Update Exception ',e)

def delete():
    print("Delete operation")
    db_cursor = _connection.cursor()
    id = raw_input("\n\tEnter rollno to delete ::: \t")
    delete_query = 'DELETE from student where rollno='+str(id)
    try:
        db_cursor.execute(delete_query)
        _connection.commit()
        read()
    except Error as e:
        print('Delete Exception ',e)

def bulkInsert():
    print('Bulk insert from Rest API')
    bulkdata = []
    response = requests.get("https://jsonplaceholder.typicode.com/users").json()
    for record in response:
            tuple = (record['id'],record['username'],record['website'])
            bulkdata.append(tuple)
    # print(bulkdata)

    db_cursor = _connection.cursor()
    try:
        sql = "INSERT INTO student (rollno, name, address) VALUES (%s, %s, %s)"
        db_cursor.executemany(sql, bulkdata)
        _connection.commit()
        print(db_cursor.rowcount, "rows was inserted.")
        1
    except Error as e:
        print('unable to insert ', e)

def main():
    print('Select DB operation\n 1. Create \n 2. Read \n 3.Update \n 4.Delete \n 5.List DB \n 6. Create DB \n 7.Drop DB \n 8.Create Table \n9.Bulk insert\n Press other to quit')

    print('--------------------------------')

    while True:

        opr = input("Enter operation  :::: \t")
        #DB Connection Establishment
        connectDB()
        print('--------------------------------')
        if opr == 1:
            create()
        elif opr == 2:
            read()
        elif opr == 3:
            update()
        elif opr == 4:
            delete()
        elif opr == 5:
            dbList()
        elif opr ==6:
            dbCreate()
        elif opr == 7:
            dropDB()
        elif opr == 8:
            createTable()
        elif opr ==9:
            bulkInsert()
        else:
            print("Exit Operation")
            break

    closeConnection()
    print("EOP :)")

if __name__ == "__main__":
    main()
