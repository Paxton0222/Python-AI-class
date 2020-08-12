import pandas as pd
import numpy as np

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

columns =["city","name", "population"]
# 建立空的DataFrame物件
df_empty = pd.DataFrame(np.nan, index=ordinals, columns=columns) #建立空的資料 並且設定 index and colums
print(df_empty)
# 複製DataFrame物件
df_copy = df.copy() # copy 顧名思義
print(df_copy)