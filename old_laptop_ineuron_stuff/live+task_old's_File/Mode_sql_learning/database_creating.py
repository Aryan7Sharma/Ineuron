import mysql.connector
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='Elon@2003')
    print(mydb)
    mycursor=mydb.cursor()
    #mycursor.execute("create database tutorials")
    mycursor.execute("show databases")
    for i in mycursor.fetchall():
        print(i)
    mydb.close()
except Exception as e:
    print(e)
