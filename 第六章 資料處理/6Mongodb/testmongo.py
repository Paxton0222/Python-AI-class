import pymongo
#查詢json資料
client = pymongo.MongoClient("localhost",27017)
db = client.mydb
collection = db.students
#std = collection.find_one({"name":"Paxton Li"})
#print(std)
for i in collection.find({"gender":"m"}):
    print(i)
