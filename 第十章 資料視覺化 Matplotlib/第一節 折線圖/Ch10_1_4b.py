import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o", label="sin(x)")
plt.plot(x, cosinus, "g--", label="cos(x)")
plt.legend(loc=2) #指定 loc 參數值為 2(左上)
plt.xlabel("Rads")
plt.ylabel("Amplitude")
plt.title("Sin and Cos Waves")
plt.show()

