import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(6,4), columns=list("ABCD")) #建立 6*4 dataframe columns 為 list abcd
# 用 rand() 函數 隨機取值 0.0-1.0
print(df)
df.to_html("Ch9_5_3_01.html")
# 套用 numpy.cumsum 函數 做累加計算 由上而下累加 2=1+2 3=1+2+3 以此類推...
df2 = df.apply(np.cumsum) 
print(df2)
df2.to_html("Ch9_5_3_02.html")
# 使用 lambda 運算式 計算 最大和最小值的差
df3 = df.apply(lambda x: x.max() - x.min())
print(df3)
