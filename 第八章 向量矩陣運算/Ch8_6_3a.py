import numpy as np
#numpy的四捨五入
a = np.array([1.0,5.55, 123, 0.567, 25.532]) 
print("a=" + str(a))

print(np.around(a))#預設值 0 沒有小數
print(np.around(a, decimals = 1)) #小數點下一位
print(np.around(a, decimals = -1)) #10進位

a = np.array([-1.7, 1.5, -0.2, 0.6, 10]) 
print("a=" + str(a))

b = np.floor(a) #取最小整數，即刪除小數
print("floor()=" + str(b))
b = np.ceil(a) #取最大整數，有小數直接進位
print("ceil()=" + str(b))