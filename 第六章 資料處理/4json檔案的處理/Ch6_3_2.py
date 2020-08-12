import json

data = {
   "name": "Joe Chen", 
   "score": 95, 
   "tel": "0933123456"         
}
json_str = json.dumps(data) #使用 dumps() 把 JSON 字典 轉成 字串
print(json_str)
print(type(json_str))
data2 = json.loads(json_str)
print(data2)
print(type(data2))

for i in data2:
   print(data2[i],end=",")