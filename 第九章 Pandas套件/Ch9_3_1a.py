import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df[0:3])                # 不含 3 使用預設的索引去搜索
print(df["sixth":"eleventh"]) # 含 "eleventh" #使用自建的索引去搜索
df[0:3].to_html("Ch9_3_1a_01.html")
df["sixth":"eleventh"].to_html("Ch9_3_1a_02.html")