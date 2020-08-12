import requests

r = requests.get("http://www.flag.tw")

fp = open("flag.txt", "w", encoding="utf8") #使用 open方法 建立檔案 mode = 'w' 覆蓋寫入模式，寫入時檔案指針在檔頭 編碼方式=utf8
fp.write(r.text) #進行寫入動作
print("寫入檔案flag.txt...")
fp.close() #關閉檔案
#相對路徑 ./flag.txt    ./ 代表上一層資料夾
#絕對路徑 C:\Users\paxto\Desktop\題目\flag.txt
#使用方法 open(mode='w') 時，寫入的必須為 string 資料型態