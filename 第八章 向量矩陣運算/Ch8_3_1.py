import numpy as np
#利用變數指定數值和陣列做四則運算
a = np.array([1, 2, 3]) 
print("a=" + str(a))
s = 5 
print("s=" + str(s))
b = a + s       
print("a+s=" + str(b))    
b = a - s       
print("a-s=" + str(b))   
b = a * s       
print("a*s=" + str(b))  
b = a / s       
print("a/s=" + str(b))