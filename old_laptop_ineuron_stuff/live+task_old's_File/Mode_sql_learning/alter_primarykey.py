import mysql.connector
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='Elon@2003',database='tutorials')
    print(mydb)
    mycursor=mydb.cursor()
    #mycursor.execute("create database tutorials")
    mycursor.execute("alter table us_housing_units DROP PRIMARY KEY")
    print(mycursor)
    print(mycursor.fetchall())
    mydb.close()
except Exception as e:
    print(e)
