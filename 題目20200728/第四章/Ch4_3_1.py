import requests

r = requests.get("http://www.google.com.tw") 

r.encoding = 'utf8' #utf-8編碼

print(r.text) #寫出資料
print(r.encoding) #編碼代號

r = requests.get("http://www.google.com.tw")

r.encoding = 'big5' #big5編碼
print(r.text) #寫出資料
print(r.encoding) #編碼代號