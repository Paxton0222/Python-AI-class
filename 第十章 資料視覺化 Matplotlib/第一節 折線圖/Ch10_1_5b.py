import matplotlib.pyplot as plt

days = range(1, 9)
celsius_min = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
celsius_max = [27.6, 26.1, 22.5, 30.4, 29.5, 31.5, 35.1, 39.4]
plt.plot(days, celsius_min, "r-o",days, celsius_max, "g--o") #plot(x,y,linetype,x,y,linetype)
plt.xlabel("Day")
plt.ylabel("Celsius")
plt.axis([0, 10, 15, 40]) #定義軸範圍 axis([xmin,xmax,ymin,ymax])
plt.show()