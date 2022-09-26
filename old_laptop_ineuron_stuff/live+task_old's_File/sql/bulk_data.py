import mysql.connector
'''
try:
    mydb = mysql.connector.connect(host='localhost', user='root', password='Elon@2003')
    print(mydb)
    cursor=mydb.cursor()
    cursor.execute("show databases")
    print(cursor.fetchall())
    cursor.execute("create database ineuron")
    print("inuron database created")
    cursor.execute("show databases")
    print(cursor.fetchall())
    cursor.execute("use ineuron")
    print("database selected")
    mydb.close()
except Exception as e:
    print(e)
'''
import pandas as pd
df=pd.read_csv("bank/bank-full.csv",index_col=False)
l=[]
j=0
for i,row in df.iterrows():
    print(tuple(row))
    l.append(tuple(row))
    j+=1
    if j==4:break
print(l)

try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='Elon@2003',database='ineuron')
    print(mydb)
    mycursor=mydb.cursor()
    mycursor.execute("select * from banks")
    print(mycursor.fetchall())
    print("done")
    for i,row in df.iterrows():
        sql="insert into banks(age, job, marital, education, df, balance, housing, loan, contact, d, m, duration, campaign, pdays, previous, poutcome, y) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql,tuple(row))
        print("Inserted")
        mydb.commit()
    print("All data inserted successfully")
    mycursor.execute("select * from ineuron.bank_details")
    print(mycursor)
    print(mycursor.fetchall())
    for i in mycursor.fetchall():
        print(i)
    mydb.close()
except Exception as e:
    print(e)
