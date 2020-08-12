import numpy as np

a = np.array([1,2,3])
print("a=" + str(a))

b = a.copy() #複製陣列 a 
print("b=a.copy()->" + str(b))
b.fill(4) #在 b 中 所有值內填充 4 
print("b.fill(0)=" + str(b))
c = np.concatenate((a,b)) #連接 a 與 b 
print("c=np.concatenate((a,b))->" + str(c))
