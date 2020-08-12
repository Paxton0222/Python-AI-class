import pandas as pd
from numpy.random import randint

df = pd.DataFrame(columns=("qty1", "qty2", "qty3")) #新增多個 dataframe 欄位
for i in range(5): #迭代寫入五筆亂數資料，每筆資料中有三個資料欄位
    df.loc[i] = [randint(-1,1) for n in range(3)]
print(df)
df.to_html("Ch9_4_3a_01.html")

df2 = pd.DataFrame(columns=("qty1", "qty2", "qty3")) #新增多個 dataframe 欄位
for i in range(5): #另一種寫法 使用 append()函數加入 ignore_index=True
    s = pd.Series({"qty1":randint(-1,1),"qty2":randint(-1,1),"qty3":randint(-1,1)})
    df2 = df2.append(s, ignore_index=True)
print(df2)
df.to_html("Ch9_4_3a_02.html")