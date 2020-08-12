import matplotlib.pyplot as plt
import numpy as np
#亂數產生 x,y座標陣列，原點尺寸，顏色
#rand() 隨機產生 0.0-1.0
x = np.random.rand(1000) 
y = np.random.rand(1000)
size = np.random.rand(1000) * 50
color = np.random.rand(1000)
plt.scatter(x, y, size, color) #呼叫散布圖
plt.colorbar() #呼叫 色彩長條圖
plt.show()

