fp = open("flag.txt", "r", encoding="utf8") #使用方法 open(mode='r') 唯獨模式
str = fp.read() #使用方法 read() 讀取
print("檔案內容:")
print(str) #導出