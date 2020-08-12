import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50) #使用 numpy的 linspace() 函數 建立一個值為 0-10 並且平均產生 50筆資料
sinus = np.sin(x) #使用 numpy 進行 三角函數 sin() 計算
cosinus = np.cos(x) #使用 numpy 進行 三角函數 cos() 計算
plt.plot(x, sinus, x, cosinus) #plot(x,y,x,y)
plt.show()