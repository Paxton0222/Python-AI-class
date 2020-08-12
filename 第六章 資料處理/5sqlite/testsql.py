import sqlite3



def connect():
    global conn
    conn = sqlite3.connect('Books.sqlite')

def cheaksql():
    connect()
    cursor = conn.execute("SELECT * FROM Books")
    for row in cursor:
        print(row[0], row[1])
    conn.close() 

def writesql():
    connect()
    a = input('id:')
    b = input('title:')
    c = input('price:')
    d = {"id": "{a}".format(a=a),"title": "{b}".format(b=b),"price": '{c}'.format(c=c) }
    sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}',{2})"
    sql = sql.format(d['id'], d['title'], d['price'])
    try:
        cursor = conn.execute(sql)   # 執行SQL指令
        #print(cursor.rowcount) #1 代表OK，查詢是否寫入
        if cursor.rowcount == 1 :
            print('已新增至資料庫中!')
        conn.commit() # 確認交易
        conn.close()  # 關閉資料庫連接
    except:
        conn.close()  # 關閉資料庫連接

def cheaksql2():
    connect()
    data1 = input('請輸入id:')
    sql = "SELECT * FROM Books WHERE id='{data1}'".format(data1=data1)
    cursor = conn.execute(sql)
    for row in cursor:
        print(row[0],row[1])
    conn.close()

def cheaksql3():
    connect()
    data1 = input('請輸入price:')
    sql = "SELECT * FROM Books WHERE price='{data1}'".format(data1=data1)
    cursor = conn.execute(sql)
    for row in cursor:
        print(row[0],row[1])
    conn.close()

def cheaksql4():
    connect()
    data1 = input('請輸入搜尋title文字:')
    sql = "SELECT * FROM Books WHERE title LIKE '%{data1}%'".format(data1=data1)
    cursor = conn.execute(sql)
    for row in cursor:
        print(row[0],row[1])
    conn.close()

def cheaksql5():
    connect()
    data1 = input('請輸入價格(大於):')
    sql = "SELECT * FROM Books WHERE price > '{data1}'".format(data1=data1)
    cursor = conn.execute(sql)
    for row in cursor:
        print(row[0],row[1])
    conn.close()

def cheaksql6():
    connect()
    data1 = input('請輸入價格(小於):')
    sql = "SELECT * FROM Books WHERE price < '{data1}'".format(data1=data1)
    cursor = conn.execute(sql)
    for row in cursor:
        print(row[0],row[1])
    conn.close()

def createsql():
    connect()
    sql = """CREATE TABLE Books ("id" TEXT UNIQUE, "title" TEXT NOT NULL,"price" INTEGER, PRIMARY KEY('id'))"""
    cursor = conn.execute(sql)
    conn.commit()
    conn.close() 

if __name__ == '__main__':
    writesql() #寫入資料表 books
    cheaksql() #查詢資料表1
    #cheaksql2() #查詢資料表2
    #cheaksql3() #查詢資料表3
    #cheaksql4() #查詢資料表4
    #cheaksql5() #查詢資料表5
    #cheaksql6() #查詢資料表6
    #createsql() #創建資料表
    # Sqlite 介紹 http://tw.gitbook.net/sqlite/sqlite_overview.html