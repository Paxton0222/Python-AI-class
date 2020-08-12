import matplotlib.pyplot as plt

days = range(0, 22, 3)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
plt.plot(days, celsius)
xmin, xmax, ymin, ymax = -5, 25, 15, 35
plt.axis([xmin, xmax, ymin, ymax]) #使用 axis() 函數定義軸範圍
plt.show()
plt.show()