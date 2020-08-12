import requests

r = requests.get("http://www.google.com.tw")

print(r.headers['Content-Type']) #編碼類型
print(r.headers['Content-Length']) #長度
print(r.headers['Date']) #日期
print(r.headers['Server']) #伺服器名稱