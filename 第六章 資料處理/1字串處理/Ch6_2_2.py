import re

str1 = "  Python, is   a, \nprogramming, \n\nlanguage.\n\r   "

list1 = str1.split(",")
for item in list1:
    item = re.sub(r"\n+", "", item) #刪除\n
    item = re.sub(r" +", " ", item) #刪除空白
    item = item.strip() #刪除前後空白字元
    print("'" + item + "'")