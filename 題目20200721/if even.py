#奇數偶數判斷
import time
n = 1
m = 100
while n<m+1:
    if(n % 2 == 0):
        print(n,"是偶數")
    else:
        print(n,'是奇數')
    n+=1
    time.sleep(0.1)