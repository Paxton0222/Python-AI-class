import numpy as np

a = np.arange(5) #建立一個 0-4 的陣列
print(a)
b = np.arange(1, 6, 2) #建立 1-5 每次間隔 2 的數
print(b) 

c = np.zeros(2) #產生兩個是 0 的 一維陣列
print(c)  
d = np.zeros((2,2)) #產生兩個 兩個是 0 的 二微陣列
print(d)           

e = np.ones(2) #產生兩個是 1 的 一維陣列
print(e)   
f = np.ones((2,2)) #產生兩個 兩個是 1 的 二微陣列
print(f)         

g = np.full(2, 7) #產生 兩個是 7 的一維陣列 full(array,num)
print(g)      
h = np.full((2,2), 7) #產生 兩個 兩個是 7 的 二微陣列 full((array,個數),num)
print(h)  