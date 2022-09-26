import mysql.connector
# creating connection
try:
    mydb=mysql.connector.connect(host="localhost" ,user="root",password="Elon@2003")
    print(mydb)
    mycursor=mydb.cursor()
    query="show databases" # showing all databases
    mycursor.execute(query)
    for i in mycursor:
        print(i)
    mydb.close()
except Exception as e:
    print(e)

# creating connection
try:
    mydb=mysql.connector.connect(host="localhost" ,user="root",password="Elon@2003")
    print(mydb)
    mycursor=mydb.cursor()
    query="show databases" # showing all databases
    mycursor.execute(query)
    print(mycursor.fetchall())
    mydb.close()
except Exception as e:
    print(e)

# creating connection with specified databases
try:
    mydb=mysql.connector.connect(host="localhost" ,user="root",password="Elon@2003",database="mysql")
    print(mydb)
    mycursor=mydb.cursor()
    query="show tables;" # showing all tables in mysql_databases
    mycursor.execute(query)
    print(mycursor.fetchall())
    mydb.close()
except Exception as e:
    print(e)

# creating database and table
try:
    mydb=mysql.connector.connect(host="localhost" ,user="root",password="Elon@2003")
    print(mydb)
    mycursor=mydb.cursor()
    mycursor.execute(" create database aryan") # creating databases
    print(mycursor.fetchall())
    mycursor.execute(" create table aryan.ineuron(employee_id int PRIMARY KEY,ename varchar(50),emp_mailid varchar(100),emp_salary int);")
    print(mycursor.fetchall())
    mydb.close()
except Exception as e:
    print(e)

#