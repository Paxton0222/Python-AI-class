import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 50) #使用 numpy 計算 2*圓周率 並從中取得 50 個平均值
y = np.sin(x) #x 的 sin() 計算
plt.scatter(x, y) #scatter()函數為 "散布圖" scatter(x,y)
plt.show()