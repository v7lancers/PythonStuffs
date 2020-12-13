import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

print(database) #Connection Object will be printed
