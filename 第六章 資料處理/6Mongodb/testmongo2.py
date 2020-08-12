import pymongo
#加入json資料
client = pymongo.MongoClient("localhost",27017)
db = client.mydb
collection = db.students

std = {
    'name':'mary wang',
    'dob':'2020/07/28',
    'gender':'f',
    'favorite_color':'red',
    'nationality':'taiwan'
}

result = collection.insert_one(std)
print('新增一筆資料:{0}'.format(result.inserted_id)) #Object id