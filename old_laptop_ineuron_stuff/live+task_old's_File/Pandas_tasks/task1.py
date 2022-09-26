import collections

import pandas as pd
import logging
import mysql.connector
logging.basicConfig(filename="log.txt",level=logging.DEBUG,format='%(asctime)s - %(message)s - %(levelname)s', datefmt=('%d-%b-%y %H:%M:%S'))
import pymongo


class Pandas_task:
    logger=logging.getLogger()
    logger.info("Now i'm inside a class")
    mydb = mysql.connector.connect(host='localhost', user='root', password='Elon@2003', database='ineuron')
    logger.info("now mysql is connected with the ineuron database  --%s", mydb)
    cursor = mydb.cursor()

    # 1. Create a  table for attribute dataset and dress dataset
    try:
        logger.info("Now im inside a try block")
        def create_tables(self):
            self.logger.info("now im creating an table for attribute dataset and dress dataset")
            mydb=mysql.connector.connect(host="localhost",user="root",password="Elon@2003",database="ineuron")
            self.logger.info("%s",mydb)
            cursor=mydb.cursor()
            self.logger.info("database connected")
            cursor.execute("Show Tables")
            self.logger.info("tables --%s", cursor.fetchall())
            cursor.execute("create table if not exists ineuron.attributes_data(Dressid bigint,Style varchar(100),Prices varchar(100),Ratings float(10,2),Sizes varchar(100),Season varchar(100),NeckLine varchar(100),Sleevelength varchar(100),waiseline varchar(100),Material varchar(100),Fabrictype varchar(100),Decoration varchar(100),Patterntype varchar(100),Recommendation int);")
            self.logger.info("attribute table created successfully")
            cursor.execute("create table if not exists dress_sales(Dress_ID int,29_8_2013 int,31_8_2013 int,2013_02_09 int,2013_04_09 int,2013_06_09 int,2013_08_09 int,2013_10_09 int,2013_12_09 varchar(100),14_9_2013 varchar(100),16_9_2013 varchar(100),18_9_2013 varchar(100),20_9_2013 varchar(100),22_9_2013 varchar(100),24_9_2013 int,26_9_2013 float(10,2),28_9_2013 int,30_9_2013 float(10,2),2013_02_10 float(10,2),2013_04_10 float(10,2),2013_06_10 int,2010_08_10 float(10,2),2013_10_10 float(10,2),2013_12_10 int)")
            self.logger.info("dress table created successfully")
            cursor.execute("SHOW TABLES")
            self.logger.info("All Tables of ineuron database")
            self.logger.info("%s",cursor.fetchall())
            mydb.close()
    except Exception as e:
        logger.exception(e)

    # 2. Do a bulk load for these two table for respective dataset
    try:
        logger.info("This is a try block of bulk load function")
        def bulk_load(self,query,data,tb):
            self.logger.info("now im inside a bulk load function")
            mydb=mysql.connector.connect(host='localhost',user='root',password='Elon@2003',database='ineuron')
            self.logger.info("now mysql is connected with the ineuron database  --%s",mydb)
            cursor=mydb.cursor()
            for i,row in data.iterrows():
                cursor.execute(query,tuple(row))
                self.logger.info("data inserted  --%s",cursor.fetchall())
                mydb.commit()
            self.logger.info("all data inserted successfully in -%s  ",tb)
            cursor.execute("select * from ineuron.{0}".format(tb))
            for i in cursor.fetchall():
                self.logger.info("%s",i)
            mydb.close()
    except Exception as e:
        logger.exception(e)


    # 3. read these dataset in pandas as a dataframe
    try:
        logger.info("Now im inside a try block of read a table of database in pandas dataframe")
        def read_sql_data(self,q1=None,tn1=None,q2=None,tn2=None):
            self.logger.info("Now im inside a read_sql_data function")
            self.cursor.execute(q1)
            df1=pd.DataFrame(self.cursor.fetchall(),columns=['Dress_ID','Style','Price','Rating','Size','Season','NeckLine','SleeveLength','waiseline','Material','FabricType','Decoration','Pattern Type','Recommendation'],)
            if q2 is None:
                return df1
            df1.to_csv("{0}.csv".format(tn1))
            self.logger.info("%s",df1)
            self.cursor.execute(q2)
            df2 = pd.DataFrame(self.cursor.fetchall(),columns=['Dress_ID','29_8_2013','31_8_2013','2013_02_09','2013_04_09','2013_06_09','2013_08_09','2013_10_09','2013_12_09','14_9_2013','16_9_2013','18_9_2013','20_9_2013','22_9_2013','24_9_2013','26_9_2013','28_9_2013','30_9_2013','2013_02_10','2013_04_10','2013_06_10','2010_08_10','2013_10_10','2013_12_10'])
            df2.to_csv("{0}.csv".format(tn2))
            self.logger.info("%s", df2)
            self.mydb.close()
    except Exception as e:
        logger.exception(e)

    # 4. Convert attribute dataset in json format
    try:
        logger.info("Now i'm in try block of  converting into json function ")
        def convert_into_json(self):
            self.logger.info("Now i'm inside a convert_into_json function")
            data=pd.read_csv("attributes_data.csv")
            json_data=data.to_json(orient='records')
            self.logger.info("attribute table converted in json file successfully")
            self.logger.info("%s",json_data)
            return json_data
    except Exception as e:
        logger.exception(e)

    # 5. Store this dataset into mongodb
    try:
        logger.info("Now im inside a try block of insert data into mongodb function")
        def create_table_in_mongodb(self):
            client = pymongo.MongoClient("mongodb+srv://aryan:Elon2003@cluster0.obq5u.mongodb.net/?retryWrites=true&w=majority")
            m_db=client.test
            self.logger.info("collection stablished with mongodb --%s--",m_db)
            databases=client['tasks_database']
            collection1=databases['pandas_task']
            datass=self.convert_into_json()
            self.logger.info("--all good--")
            self.logger.info("%s",datass)
            self.logger.info("Now we have data in json format--")
            collection1.insert_many(datass)
            self.logger.info("All json data inserted in mongodb successfully")
            record=collection1.find()
            for i in record:
                self.logger.info("-%s-",i)
    except Exception as e:
        logger.exception(e)

    # 6. in sql task try to perform left join operation with attrubute dataset and dress dataset on column Dress_ID
    try:
        logger.info("")
        def create_table(self):
            self.logger.info("")
            pass
        pass
    except Exception as e:
        logger.exception(e)

    # 7. Write a sql query to find out how many unique dress that we have based on dress id
    try:
        logger.info("")
        def create_table(self):
            self.logger.info("")
            pass
        pass
    except Exception as e:
        logger.exception(e)

    # 8. Try to find out how mnay dress is having recommendation 0
    try:
        logger.info("")
        def create_table(self):
            self.logger.info("")
            pass
        pass
    except Exception as e:
        logger.exception(e)

    # 9. Try to find out total dress sell for individual dress id
    try:
        logger.info("")
        def create_table(self):
            self.logger.info("")
            pass
        pass
    except Exception as e:
        logger.exception(e)

# 10. Try to find out a third highest most selling dress id
    try:
        logger.info("")
        def create_table(self):
            self.logger.info("")
            pass
        pass
    except Exception as e:
        logger.exception(e)

obj=Pandas_task()
obj.create_tables()
#data=pd.read_csv("attribute_data.csv",index_col=False)
#query="insert into attributes_data(Dressid, Style, Prices, Ratings, Sizes, Season, NeckLine, Sleevelength, waiseline, Material, Fabrictype, Decoration, Patterntype, Recommendation) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#tb="attributes_data"
#data=pd.read_csv("dress-sales.csv",index_col=False)
#query="insert into dress_sales(Dress_ID,29_8_2013,31_8_2013,2013_02_09,2013_04_09,2013_06_09,2013_08_09,2013_10_09,2013_12_09,14_9_2013,16_9_2013,18_9_2013,20_9_2013,22_9_2013,24_9_2013,26_9_2013,28_9_2013,30_9_2013,2013_02_10,2013_04_10,2013_06_10,2010_08_10,2013_10_10,2013_12_10) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#tb="dress_sales"
#obj.bulk_load(query,data,tb)
#query1='''select * from ineuron.attributes_data'''
#query2='''select * from ineuron.dress_sales'''
#tn1="attributes_data"
#tn2="dress_sales"
#obj.read_sql_data(query1,tn1,query2,tn2)
#obj.create_table_in_mongodb()
