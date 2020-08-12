with open("flag.txt", "r", encoding="utf8") as fp: #with as 方法 唯獨模式
    list1 = fp.readlines() #一次只讀一行
    for line in list1: #迴圈取得資料
        print(line, end="")