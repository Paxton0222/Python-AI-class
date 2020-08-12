import numpy as np
#陣列平坦化(降維)
a = np.array([[1,2,3],[4,5,6]])
print("a=")
print(a)

b = a.ravel() #平坦化陣列
print("a.ravel()=" + str(b))
b = np.ravel(a) #不同的寫法
print("np.ravel(a)=" + str(b))