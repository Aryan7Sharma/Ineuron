import pymongo
client = pymongo.MongoClient("mongodb+srv://aryan:Elon2003@cluster0.obq5u.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

hashmap={
    "name":["risha sharma"],
    'email':["risha123@gmail.com"],
    "surname":["sharma"]
}

list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]
database=client['database1']
collection=database['2table']
#collection.insert_one(hashmap)
#collection.insert_many(list_of_records)
#data1={"packetType":"D","data":{"checkEngineLightFlag":"F","batteryVoltageStableTime":0,"batteryVoltageStable":"0","batteryVoltageOff":"12.42","batteryCrankParamTN":"-0.08","batteryCrankParamVN":"0.00","batteryCrankParamTP":"-0.08","batteryCrankParamVP":"0.00","batteryCrankParamTT":"-0.00008","batteryCrankParamV0":"0.00","batteryVoltageMaxOn":"13.05","batteryVoltageMinOn":"12.97","batteryVoltageMaxOff":"12.46","batteryVoltageMinOff":"12.36","batteryVoltageOnAverage":"13.02","engineLoadMax":"84","engineLoadAverage":"39.98","rpmMax":"3487","rpmAverage":"1431.29","gpsSpeedAverage":"21.99","vssMax":"53.44","vssAverage":"23.06","tcuTemperatureMin":"82.40","tcuTemperatureMax":"109.40","tcuTemperatureAverage":"104.87","coolantMin":"158.00","coolantMax":"188.60","coolantAverage":"180.20","packetStartLocal":1508143346000,"tripStartLocal":1508143346000,"milIndicator":"F","monitorsNotReady":0,"imei":"60DF5417","gatewayTs":1515613306592,"diagnosticTroubleCodeData":[345345],"diagnosticPidData":[[64768,47,100],[64768,1,517376],[64800,1,262144],[64768,5,125]]},"header":{"iwrapVer":"1.9.20","sourceSystem":"CDP","configVer":"1.1","oemName":"HUM","unitType":0,"cpVer":"7.50.1.9","igpsVer":"1.3.7","messageType":"Notification","pomVer":"1.0","headerVer":"V6","timestamp":0,"deviceType":"InDrive","visorVer":"1.4.35","transactionId":"53098471-7787-4160-94b3-cd69dcc70416","deviceSerialNo":"60DF5417","subOrganization":"HUM","organization":"HUM","imei":"60DF5417","operation":"Notification"}}
#collection.insert_one(data1)


'''
# fetch all data of table1
records=collection.find()
for i in records:
    print(i)

# fetch only those data where (product is 'Affordable AI') in table 1
data=collection.find({"product":"Affordable AI"})
for j in data:
    print(j)

# fetch only those data where course name is greater than (E)
datas=collection.find({"courseOffered":{"$gt":"E"}})
for i in datas:
    print(i)
    
'''
#make new table
collection1=database["3table"]

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

'''
client = pymongo.MongoClient("mongodb+srv://ineuron:ineuron1@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['inventory']
collection = database["table"]
#collection.insert_many(data)
#d = collection.find({'status':'A'})
#d = collection.find({'status':{'$in':['A' , 'P']}})
#d = collection.find({'status':{"$gt" : "C"}})
#d = collection.find({'qty':{'$gte' :75}})
#d = collection.find({'item': 'sketch pad','qty': 95})
#d = collection.find({ 'item': 'sketch pad' , 'qty' :{"$gte" : 75}})
#d = collection.find({'$or' : [{ 'item': 'sketch pad'} , {'qty': {"$gte": 75}}]})
#collection.update_one({'item': 'canvas'} , {'$set':{'item': 'sudhanshu'} })
collection.delete_one({'item': 'sudhanshu'})
d = collection.find({'item': 'sudhanshu'})
for i in d :
    print(i)


'''

#collection1.insert_many(data)
#d=collection1.find()
#d=collection1.find({'status':'P'})
#d=collection1.find({'item':'sketch pad','qty':95})
#d=collection1.find({'$or':[{'item':'sketch pad'},{'qty':{"$gte":99}}]})
#collection1.update_one({'item':'canvas'},{"$set":{'item':'aryan_sharma'}})

collection1.delete_one({'item':'aryan_sharma'})
d=collection1.find({'item':'aryan_sharma'})

for i in d:
    print(i)