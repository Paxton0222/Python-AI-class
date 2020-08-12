import numpy as np
#走訪二微陣列的元素
a = np.array([[1, 2], [3, 4], [5, 6]])
for ele in a:
    print(ele)
#巢狀迴圈走訪二維陣列
for ele in a:
    for item in ele:
        print(str(item) + " ", end="")
print()
for i in a:
    for b in i:
        print(str(b),end=" ")