import numpy as np

a = np.array([1,2,3])
print("a=" + str(a))

b = a[:, np.newaxis]  #新增陣列維度 定義全部 0-2 為新的陣列維度 y 
print("b=a[:,np.newaxis]->")
print(b)
print(b.shape) #查看陣列維度
b = a[np.newaxis, :] #新增陣列維度 定義全部 0-2 為新的陣列維度 x 
print("b=a[np.newaxis,:]->")
print(b)
print(b.shape)