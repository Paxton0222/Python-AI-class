import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(5, 1500, size=(2,3))) #隨機取值成 dataframe 並且為 2*3
print(df)
df.to_html("Ch9_4_1c_01.html")
# 取得與更新整個DataFrame
print(df[df > 800]) #大於 800 的寫出來
df[df > 800].to_html("Ch9_4_1c_02.html")
df[df > 800] = df - 100 #大於 800 的 -100
print(df)
df.to_html("Ch9_4_1c_03.html")