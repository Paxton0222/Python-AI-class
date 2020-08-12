import pandas as pd

fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
quantities = [15, 33, 45, 55]
s = pd.Series(quantities, index=fruits) 
p = pd.Series([11, 16, 21, 32], index=fruits) 
print(s + p) #把 s 跟 p 做相加
print("總計=", sum(s + p))
