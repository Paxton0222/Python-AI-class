import requests
#使用例外處理
try:
    r = requests.get("http://www.google.com", timeout=0.03) #設定時間上限0.03秒
    print(r.text)
except requests.exceptions.Timeout as ex: #如果傳送請求後，伺服器回傳超過時間
    print("錯誤: HTTP請求已經超過時間...\n" + str(ex))
#else
#finally
