import numpy as np
#建立一個 二維陣列 
a = np.array([[1,2,3],[4,5,6]])
print(a[0, 0], a[0, 1], a[0, 2])
print(a[1, 0], a[1, 1], a[1, 2])
a[0, 0] = 6 #6 2 3
a[1, 2] = 1 #4 5 1
print(a)
