print('執行四則運算+,-,*,/')
x=int(input("請輸入第一個值:"))
z=input("請輸入要執行的運算類型+,-,*,/:")
y=int(input("請輸入第二個值:"))
if z == "+":
    print("第一個值加上第二個值的答案是:",(x+y))
    print('運算完成!')
elif z == "-":
    print("第一個值跟第二個值相減的答案是:",(x-y))
    print('運算完成!')
elif z == "*":
    print("第一個值乘上第二個值的答案是:",(x*y))
    print('運算完成!')
elif z == "/":
    print("第一個值除以第二個值的答案是:",(x/y))
    print('運算完成!')
else:
    print("不支援此類型的運算!")