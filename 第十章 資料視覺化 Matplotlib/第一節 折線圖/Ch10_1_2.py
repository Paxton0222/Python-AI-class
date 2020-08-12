import matplotlib.pyplot as plt
import numpy as np
#課本 10-5 頁 詳細介紹
x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o",x, cosinus, "g--")
plt.show()

