import re

phone = "0938-111-4567 # Pyhone Number"

num = re.sub(r"#.*$", "", phone) #  刪除"#"" , "."代表刪除換列字元 , "*" 代表前一個項目可以出現無限多次 , "$"代表輸入列結束
print(num)
num = re.sub(r"\D", "", phone) #刪除非數字字元 相當於 ^[0-9] , "^" 是反運算
print(num)