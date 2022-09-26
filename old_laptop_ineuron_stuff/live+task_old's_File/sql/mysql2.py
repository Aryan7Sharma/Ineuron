import mysql.connector
# inserting data into the table
'''
try:
    mydb=mysql.connector.connect(host="localhost" ,user="root",password="Elon@2003",database="aryan")
    print(mydb)
    mycursor=mydb.cursor()
    sql = "INSERT INTO ineuron (employee_id,ename ,emp_mailid,emp_salary) VALUES (%s, %s, %s, %s)"
    val = [
        ('1','Peter', 'Lowstreet','40000'),
        ('2','aryan', 'reet', '400000'),
        ('3','rohan', 'Low', '100000'),
        ('4','krishna', 'street', '80000'),
    ]
    mycursor.executemany(sql,val)
    mydb.commit()
    mydb.close()
except Exception as e:
    print(e)
'''
# access the whole data of a specific table
'''
try:
    mydb=mysql.connector.connect(host="localhost" ,user="root",password="Elon@2003",database="aryan")
    print(mydb)
    mycursor=mydb.cursor()
    mycursor.execute("select * from ineuron;")
    for i in mycursor.fetchall():
        print(i)
    mydb.close()
except Exception as e:
    print(i)
'''

# access the whole data of a specific table
try:
    mydb=mysql.connector.connect(host="localhost" ,user="root",password="Elon@2003",database="aryan")
    print(mydb)
    mycursor=mydb.cursor()
    mycursor.execute("select ename,emp_salary from ineuron;")
    for i in mycursor.fetchall():
        print(i)
    mydb.close()
except Exception as e:
    print(i)


# access the whole data of a specific table
l=[]
try:
    mydb=mysql.connector.connect(host="localhost" ,user="root",password="Elon@2003",database="aryan")
    print(mydb)
    mycursor=mydb.cursor()
    mycursor.execute("select ename,emp_salary from ineuron;")
    for i in mycursor.fetchall():
        temp=[]
        temp.append(i[0])
        temp.append(i[1])
        l.append(temp)
    mydb.close()
    print(l)
except Exception as e:
    print(i)

# access the whole data of a specific table
try:
    mydb=mysql.connector.connect(host="localhost" ,user="root",password="Elon@2003",database="aryan")
    print(mydb)
    mycursor=mydb.cursor()
    mycursor.execute("select ename,emp_salary from ineuron;")
    for i in mycursor.fetchall():
        temp=[]
        temp.append(i[0])
        temp.append(i[1])
        print(temp)
    mydb.close()
except Exception as e:
    print(i)