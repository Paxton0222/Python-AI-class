import numpy as np
#建立陣列
a = np.array([1, 2, 3, 4, 5]) 
b = np.array((1, 2, 3, 4, 5)) 
print(type(a))  #查看資料型態
print(type(b))  #查看資料型態      
print(a[0], a[1], a[2], a[3], a[4]) #依序取出 a 的 資料
b[0] = 5    #定義 b[0] 是 5 
print(b) 
b[4] = 0    #定義 b[4] 是 0 
print(b)    