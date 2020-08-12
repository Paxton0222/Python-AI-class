import requests

url = "https://api.github.com/user"

r = requests.get(url, auth=('hueyan@ms2.hinet.net', '********')) #傳送使用者資訊
if r.status_code == requests.codes.ok: #如果http狀態碼 為 200
    print(r.headers['Content-Type']) 
    print(r.json())
else:
    print("HTTP請求錯誤...")