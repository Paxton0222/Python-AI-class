import matplotlib.pyplot as plt

data = [-1, -4.3, 15, 21, 31] #使用list設定一個圖表值
print(type(data))
plt.plot(data)  # x軸是 0,1,2,3,4 劃出一個線性圖表
plt.show() #顯示出來 " 如果需要顯示就一定要加入此項指令 "