import pandas as pd
from numpy.random import randint

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

df["area"] = pd.Series([randint(6000,9000) for n in range(len(df))]).values  #新增一個 area 的數值到 df 中
print(df.head())
df.head().to_html("Ch9_4_3b_01.html")
df.loc[:,"zip"] = randint(100, 120, size=len(df)) #使用 loc()函數 新增一個 zip 的數值到 df 中
print(df.head())
df.head().to_html("Ch9_4_3b_02.html")