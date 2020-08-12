import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

print("資料數= ", len(df)) #資料長度
print("形狀= ", df.shape)  
df.info() #dataframe 具體資x