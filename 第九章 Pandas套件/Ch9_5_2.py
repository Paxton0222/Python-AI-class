import pandas as pd

products = pd.DataFrame({ #建立dataframe
        "分類": ["居家", "居家", "娛樂", "娛樂", "科技", "科技"],
        "商店": ["家樂福", "頂好", "家樂福", "全聯", "頂好","家樂福"],
        "價格":[11.42, 23.50, 19.99, 15.95, 55.75, 111.55],
        "測試分數": [4, 3, 5, 7, 5, 8]})
print(products)
"""
df = products.groupby(['商店','分類']).sum()
df = df.pivot_table(index='商店')
print(df)
"""
products.to_html("Ch9_5_2_01.html")
# 呼叫 pivot_table() 方法
# pivot_table() 是使用定義索引，欄位，資料來 重塑 dataframe
#下面定義了 索引為'分類' 欄位為'商店' 資料為'價格'
pivot_products = products.pivot_table(index='分類',columns='商店',values='價格')
print(pivot_products)
pivot_products.to_html("Ch9_5_2_02.html")