#質數公式: 2,n範圍內，檢查範圍內的數不可被n的開根號整除。
#質數是甚麼?
#質數是大於1，且只含有1和本身兩個因數的數
#例如:2的因數只有2跟1，3的因數只有1跟3
#1本身不是質數
#2是所有質數中唯一的偶數

#1寫出一個巢狀for迴圈，判斷10-20範圍內的數是否為質數，並且在第二個迴圈中，加入if else判斷式去判斷是否為質數。
for num in range(10,20):#輸入範圍
   for i in range(2,num):  #從2開始依序循環
      if num%i == 0:     #用判斷式確定第一個因子
         j=num/i  #計算第二個因子
         print('%d 等於 %d * %d' % (num,i,j)) #%d 為導入參數num,i,j的用法
         break   #跳出第2個迴圈，回到第一個繼續循環
   else:                  
      print(num, '是一個質數')

#2根據第一題，加入input()函式給使用者輸入數值
n = input('輸入起始數:')
m = input('輸入最終數:')
for num in range(int(n),int(m)+1):#輸入範圍
   for i in range(2,num):  #從2開始依序循環
      if num%i == 0:     #用判斷式確定第一個因子
         j=num/i  #計算第二個因子
         print('%d 等於 %d * %d' % (num,i,j))
         break   #跳出第2個迴圈，回到第一個繼續循環
   else:                  
      print(num, '是一個質數')

#3使用物件導向，實現單個數字的質數計算程式，並使用return方法輸出布林值
def is_prime1(y):#y=11
    for i in range(2, y):
        if y % i == 0:  # 整除，i 是 n 的因數，所以 n 不是質數。
            return False
    return True     # 都沒有人能整除，所以 n 是質數。
x=11
print(is_prime1(y=n))

#4承接第3題，利用輸出的布林值，寫出if else 判斷式
#x= input('輸入一個數:')
x = 15       #15
if is_prime1(int(x)) == True: #ans1-2
    print(str(x),'是一個質數')
else:
    print('不是一個質數')

#5根據第2題，使用物件導向，寫出範圍值內的計算值數函式並且輸出。
#ans2
n = input('輸入起始數:')
m = input('輸入最終數:')
def is_prime2(n,m):
    for num in range(int(n),int(m)):
        for i in range(2, num):
            if num % i == 0:  # 整除，i 是 n 的因數，所以 n 不是質數。
                j=num/i  
                print('%d 等於 %d * %d' % (num,i,j))
                break
        else:
            print(num, '是一個質數')     # 都沒有人能整除，所以 n 是質數。
