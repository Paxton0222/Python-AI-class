import numpy as np
#向量點積運算(對應向量與向量加總的乘積和)
#b = a*s = a1*s1+a2*s2+a3*s3
a = np.array([1, 2, 3]) 
print("a=" + str(a))
s = np.array([4, 5, 6])  
print("s=" + str(s))
b = a.dot(s)       
print("a.dot(s)=" + str(b))    
