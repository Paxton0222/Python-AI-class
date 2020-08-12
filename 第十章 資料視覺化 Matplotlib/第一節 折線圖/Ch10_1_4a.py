import matplotlib.pyplot as plt
import numpy as np
#legend() 函數 還可以指定 loc參數指定位址 詳細參考 課本 10-10 頁
#loc=0 為自動選擇最佳位置
x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o", label="sin(x)")
plt.plot(x, cosinus, "g--", label="cos(x)")
plt.legend(loc=1) #指定 loc 參數值為 1(右上)
plt.xlabel("Rads")
plt.ylabel("Amplitude")
plt.title("Sin and Cos Waves")
plt.show()

