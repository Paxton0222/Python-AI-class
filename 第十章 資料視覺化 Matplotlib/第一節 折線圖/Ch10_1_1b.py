import matplotlib.pyplot as plt

days = range(0, 22, 3) #使用 range()函數 0-22 每次間隔 3 
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
plt.plot(days, celsius) #plot(x,y)
plt.show()