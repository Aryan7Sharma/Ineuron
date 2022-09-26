import mysql.connector
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='Elon@2003',database='ineuron')
    print(mydb)
    mycursor=mydb.cursor()
    mycursor.execute("create table banks(age int, job varchar(50), marital varchar(50), education varchar(100), df varchar(50), balance int, housing varchar(50), loan varchar(50), contact varchar(50), d int, m varchar(50), duration int, campaign int, pdays int, previous int, poutcome varchar(30), y varchar(30))")
    print(0)
    mycursor.execute("show databases;")
    print(1)
    for i in mycursor.fetchall():
        print(i)
    mydb.close()
except Exception as e:
    print(e)