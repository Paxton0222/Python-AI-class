import numpy as np
#rand(row,col)
a = np.random.rand(5) #產生5個0.0-1.0的亂數一維陣列
print("np.random.rand(5)=")
print(a)
b = np.random.rand(3, 2)  #產生3個 裡面有兩的數值的 二維陣列
print("np.random.rand(3,2)=")
print(b)
c = np.random.randint(5, 10, size=5) #產生randint(min,max,size)之間的亂數整數(不包含max)
print("np.random.randint(5,10,size=5)")
print(c)
d = np.random.randint(5, 10, size=(2,3))#size(y,x)
print("np.random.randint(5,10,size=(2,3))")
print(d)