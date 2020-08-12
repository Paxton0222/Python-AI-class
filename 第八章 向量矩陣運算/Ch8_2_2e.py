import numpy as np

a = np.arange(16) #產生 0-15 的一維陣列
print(a)
b = a.reshape((4, 4)) #呼叫 a 並產生 4個數為一組陣列的 二維陣列 reshape(y,x)
print(b)

c = np.array(range(10), float) #產生資料型態為 float 並且是 0-9 的一維陣列
print(c)
d = c.reshape((5, 2)) #呼叫 b 並產生 2個數為一組陣列的 二維陣列 reshape(y,x)
print(d)

