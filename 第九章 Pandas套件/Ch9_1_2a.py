import pandas as pd
#自定義 series 索引值
fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
quantities = [15, 33, 45, 55]
s = pd.Series(quantities, index=fruits) 
print(s)
print(s.index) #查看索引值
print(s.values)  #查看資料
print(s['蘋果']) #搜尋 索引值為蘋果的資料