import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c = np.concatenate((a,b)) #連接兩個二微陣列
print("c=np.concatenate((a,b))->")
print(c)
c = np.concatenate((a,b), axis=0) #設定直向連接
print("c=np.concatenate((a,b), axis=0)->")
print(c)
c = np.concatenate((a,b), axis=1) #設定橫向連接
print("c=np.concatenate((a,b), axis=1)->")
print(c)