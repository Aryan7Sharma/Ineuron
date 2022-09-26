import mysql.connector
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='Elon@2003',database='tutorials')
    print(mydb)
    mycursor=mydb.cursor()
    #mycursor.execute("create table ")
    mycursor.execute("select * from us_housing_units limit 5")
    print(mycursor)
    for i in mycursor.fetchall():
        print(i)
    mycursor.execute("select * from us_housing_units where month=3 and year=1968")
    print(mycursor)
    print(mycursor.fetchall())

    mydb.close()
except Exception as e:
    print(e)


