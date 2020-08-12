def cul(x): #定義cul參數為 x
    s=0
    for i in range(1,x):
        s+=i
    print(s)
n = input("請輸入一個終點值:") #input()回傳str
cul(int(n)) #轉換資料型態為int

