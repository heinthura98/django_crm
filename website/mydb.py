import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='earthspirit1998'
)
#prepare a cursor object
cursorObject=dataBase.cursor()

#Create a database
cursorObject.execute('CREATE DATABASE dcrm')
print('All DONE')
