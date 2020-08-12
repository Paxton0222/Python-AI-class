import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o", label="sin(x)") #直接在 plot()裡定義標線 名字
plt.plot(x, cosinus, "g--", label="cos(x)")
plt.legend() #顯示名字
plt.xlabel("Rads")
plt.ylabel("Amplitude")
plt.title("Sin and Cos Waves")
plt.show()

