import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.zeros_like(a) #建立一個跟 a 一樣 但所有數字為 0 的二微陣列 
#print(b)

c = np.ones_like(a) #建立一個跟 a 一樣 但所有數字為 1 的二微陣列 
#print(c)

d = np.eye(3)  #產生對角線都是 1 的 陣列
#print(d)
e = np.eye(3, k=1) #指定索引 1 並從 1 開始的對角線都為 1 
#print(e)
    
f = np.random.rand(3) #隨機產生 3 個亂數為一維陣列
#print(f)
g = np.random.rand(3,3) #隨機產生 3 個 並且陣列為3個的 亂數為二維陣列
print(g)   

