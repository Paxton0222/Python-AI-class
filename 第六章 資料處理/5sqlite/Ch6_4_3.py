import sqlite3
#查詢sqlite資料庫
# 建立資料庫連接
conn = sqlite3.connect("Books.sqlite")
# 執行SQL指令SELECT
cursor = conn.execute("SELECT * FROM Books")
# 取出查詢結果的每一筆記錄
#print(cursor)
for row in cursor:
    print(row[0], row[1])
conn.close()  # 關閉資料庫連接