# importing data into database from csv file

import mysql.connector
import pandas as pd
df=pd.read_csv('us_housing_units.csv',index_col=False)
print(df.head(4))
print(df.shape)
l=[]
j=1
for i,row in df.iterrows():
    print(tuple(row))
    l.append(tuple(row))
    j+=1
    if j==4:break
print(l)

try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='Elon@2003',database='tutorials')
    print(mydb)
    mycursor=mydb.cursor()
    for i,row in df.iterrows():
        sql="insert into us_housing_units(year,month,month_name,south,west,midwest,northeast) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql,tuple(row))
        print("Inserted")
        mydb.commit()
    print("All data inserted successfully")
    mycursor.execute("select * from us_housing_units")
    print(mycursor)
    print(mycursor.fetchall())
    for i in mycursor.fetchall():
        print(i)
    mydb.close()
except Exception as e:
    print(e)