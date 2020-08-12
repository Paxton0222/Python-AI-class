import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties
#How to cheak the path? : " import Module  Module.__path__"
#line style: "-","--","-.",":"
#------------------------------------
# How to change to chinese?
# 1. C:\Windows\Fonts copy "Mircosoft JhengHei Ui"
# 2. copy to "./Python\Python38-32\lib\site-packages\matplotlib\mpl-data\fonts\ttf"
# 3. rename "msjh.ttc > DejaVu Sans.ttf"
# 4. matplotlibrc line 248  "font.family  : sans-serif" delete "#"
# 5. matplotlibrc line 255 add font.sans-serif : "Microsoft JhengHei"
# 6. matplotlibrc line 395 change axes.unicode_minus : "False"  change to other lang and delete "#"
# 7. you need import every single time "from matplotlib.font_manager import FontProperties"
# 8. and add "plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] " in your code
# 9. and add "plt.rcParams['axes.unicode_minus'] = False" in your code
# 10. and you just done!
#https://medium.com/marketingdatascience/%E8%A7%A3%E6%B1%BApython-3-matplotlib%E8%88%87seaborn%E8%A6%96%E8%A6%BA%E5%8C%96%E5%A5%97%E4%BB%B6%E4%B8%AD%E6%96%87%E9%A1%AF%E7%A4%BA%E5%95%8F%E9%A1%8C-f7b3773a889b
# --------- you to need add -----------
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
#------------- variable ---------------
listx = [1,5,7,9,13,16] #x1
listy = [15,50,80,40,70,50] #y1
listx2 = [2,6,8,11,14,16] #x2
listy2 = [10,40,30,50,80,60] #y2
#--------------- line ------------------
def line(listx,listy,listx2,listy2):
    plt.title('測試matplotlib') #標題
    plt.xlabel('x list') # x 座標名稱
    plt.ylabel('y list') # y 座標名稱
    plt.plot(listx,listy,color="blue",lw=5,ls="--",label="First Line") #plot(x,y,color,lw,ls,label)
    plt.plot(listx2,listy2,color='red',linewidth=5,linestyle="-.",label="Second Line")
    plt.legend() #顯示 label 名稱
    plt.xlim(0,20) #設置 x 座標範圍 0-20
    plt.ylim(0,100) #設置 y 座標範圍 0-100
    plt.show() #顯示
#--------------- bar -------------------
def bar(listx,listy,listx2,listy2):
    plt.title('零用金統計') #標題
    plt.xlabel('年齡')
    plt.ylabel('零用錢數目')
    plt.bar(listx,listy,label="男性")
    plt.bar(listx2,listy2,color="red",label="女性")
    plt.legend() #顯示 label 名稱
    plt.xlim(0.20)  #設置 x 座標範圍 0-20   
    plt.ylim(0,100) #設置 y 座標範圍 0-100
    plt.show() #顯示
#---------------- main -------------------
if __name__ == '__main__':
    line(listx,listy,listx2,listy2)
    #bar(listx,listy,listx2,listy)