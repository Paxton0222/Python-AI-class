import pandas as pd
import numpy as np

df = pd.DataFrame({"名稱" : ["客戶A", "客戶B", "客戶A", "客戶B",
                             "客戶A", "客戶B", "客戶A", "客戶A"],
                   "編號" : ["訂單1", "訂單1", "訂單2", "訂單3",
                             "訂單2", "訂單2", "訂單1", "訂單3"],
                   "數量" : np.random.randint(1,5,size=8),
                   "售價" : np.random.randint(150,500,size=8)})
#使用 亂數套件 建立 一維陣列 1*8 兩個
print(df)
df.to_html("Ch9_5_1_01.html")

print(df.groupby("名稱").sum()) #使用 groupby() 群組化紀錄 "名稱" 在呼叫 sum() 計算欄位值的總和
df.groupby("名稱").sum().to_html("Ch9_5_1_02.html")
print(df.groupby(["名稱","編號"]).sum()) #群組化 "名稱" "編號" 呼叫 sum() 函數計算
df.groupby(["名稱","編號"]).sum().to_html("Ch9_5_1_03.html")