import numpy as np
import pandas as pd

fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
s = pd.Series([15, 33, 45, 55], index=fruits) 
print("橘子=", s["橘子"])
print(s[["橘子","梨子","櫻桃"]])
print((s+2)*3)
print(s.apply(np.sin)) #在 pandas 中 可以用 apply() 函數 做 numpy 的數學函數
