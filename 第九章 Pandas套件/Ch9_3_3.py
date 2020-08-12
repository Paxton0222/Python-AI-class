import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

df2 = df.set_index("population") #設置索引為 "population" 
print(df2.head()) 
df2.head().to_html("Ch9_3_3_01.html")

df2.sort_index(ascending=False, inplace=True) #設置降幕排序
print(df2.head())
df2.head().to_html("Ch9_3_3_02.html")