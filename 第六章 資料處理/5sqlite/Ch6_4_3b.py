import sqlite3
#利用字典的資料，取出並匯入sql資料庫，並且加入
d = {
   "id": "P0009",
   "title": "C語言程式設計",
   "price": 400
}
# 建立資料庫連接
conn = sqlite3.connect("Books.sqlite")
# 建立SQL指令INSERT字串
sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}',{2})"
sql = sql.format(d['id'], d['title'], d['price'])
#print(sql)
try:
   cursor = conn.execute(sql)   # 執行SQL指令
   #print(cursor.rowcount) #1 代表OK，查詢是否寫入
   if cursor.rowcount == 1 :
      print('已新增至資料庫中!')
   conn.commit() # 確認交易
   conn.close()  # 關閉資料庫連接
except:
   print('檔案已在資料庫中!')
   conn.close()  # 關閉資料庫連接
