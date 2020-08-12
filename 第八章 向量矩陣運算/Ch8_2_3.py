import numpy as np
#查詢陣列的資料
a = np.array([[11, 12, 13, 14, 15], #創建一個 二維陣列
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
            [26, 27, 28, 29, 30],
            [31, 32, 33, 34, 35]])

print(type(a)) #資料型態
print(a.dtype) #查詢數字的資料型態 int 32/64 or float 32/64
print(a.size) #陣列總元素數
print(a.shape) #陣列 x,y 值
print(a.itemsize) #陣列占用位元組數
print(a.ndim) #幾維陣列?
print(a.nbytes)  #全部陣列占用位元組數