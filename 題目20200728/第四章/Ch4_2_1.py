import requests #導入requests庫
#https://requests.readthedocs.io/en/master/user/quickstart/  #requests official webpage

r = requests.get("http://www.google.com") #使用 requests庫中 get(url)方法取得資料
print(r.status_code) #http狀態碼