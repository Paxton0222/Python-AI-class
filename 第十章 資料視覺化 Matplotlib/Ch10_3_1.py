import matplotlib.pyplot as plt
import numpy as np
# subplot() 子圖表 代表在一張圖表上顯示多張圖
# 如果需要建立 兩張圖表 就需要指定大小為 2*1 並且指定排序編號 1,2
# subplot(2,1,1) #2*1  第 1 列
x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.subplot(2, 1, 1) 
plt.plot(x, sinus, "r-o")
plt.subplot(2, 1, 2)
plt.plot(x, cosinus, "g--")
plt.show()