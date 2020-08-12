import requests,time
from bs4 import BeautifulSoup

#教學用網路爬蟲範例 twse
#測試版本 2020/07/30
#server requests limit = 5 sec 3 data requests

def requests_html(url):
    r = requests.get(url)
    return r.text

def requests_binary(url):
    r = requests.get(url)
    return r.content

def download_csv(url):
    html2 = requests_binary(url)
    with open('test.csv','wb')as f:
        f.write(html2)
    return "done!"

def download_html(url):
    html = requests_html(url)
    sp = BeautifulSoup(html,'lxml')
    with open('test.html','w',encoding='utf8')as f:
        f.write(str(sp))
    return "done!"

def process_html1(url): #處理html成為串列
    html = requests_html(url)
    sp = BeautifulSoup(html,'lxml')
    data = sp.find('title').string
    th = sp.find('th').string
    th2 = sp.find_all('th')
    td = sp.find_all('td',limit=64)
    td2 = sp.find_all('td')
    td2str = th2[1].string
    td2len = td2[64:82]
    list_ = []
    list2 = []
    i = 0
    while i<64:
        data1 = td[i].string
        list_.append(data1)
        i+=1
    for n in td2len:
        data2= n.string
        list2.append(data2)
    return data,th,list_,list2,td2str

def process_data1(date,data,data2,td2str,encodeing): #處理 process_html1() 回傳的資料 並且寫入 .csv檔
    i,n,x,y = 0,4,0,3
    with open('{title}.csv'.format(title=date),'a',encoding=encodeing)as f: #加入日期
        f.write(date) #寫入資料
        f.write('\n') #加入換行
        f.close() #關閉檔案資料庫
    while True:
        while i<n:
            data1 = data[i]
            with open('{title}.csv'.format(title=date),'a',encoding=encodeing)as f: #加入主要資料
                data1 = '"'+data1+'"' #處理逗號分隔問題
                f.write(data1) #寫入資料
                f.write(',') #加入分隔逗號
                f.close() #關閉檔案資料庫
                i+=1
        with open('{title}.csv'.format(title=date),'a',encoding=encodeing)as f: #加入換行字元
            f.write('\n') #加入換行
            f.close() #關閉檔案資料庫
        n+=4
        if n == 68: #停止判斷式
            break
    #print(len(data2))
    with open('{title}.csv'.format(title=date),'a',encoding=encodeing)as f: 
        f.write('\n') #加入換行
        f.write(td2str) #寫入資料
        f.write('\n') #加入換行
        f.close() #關閉檔案資料庫
    while True:
        while x<y:
            data3 = data2[x]
            with open('{title}.csv'.format(title=date),'a',encoding=encodeing)as f:
                data3 = '"'+data3+'"' #處理逗號分隔問題
                f.write(data3) #寫入資料
                f.write(',') #加入分隔逗號
                f.close() #關閉檔案資料庫
                x+=1
        with open('{title}.csv'.format(title=date),'a',encoding=encodeing)as f:
            f.write('\n') #加入換行
            f.close() #關閉檔案資料庫
        y+=3
        if y == 21:
            break
    return "檔案已儲存至 {title}.csv!".format(title=date)

if __name__ == '__main__': #寫入一筆資料
    date = input('起輸入您的日期:')
    url = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=html&date={date}".format(date=date)
    big5 = 'big5'
    data1 = process_html1(url)
    data2 = data1[2] #主資料1
    data3 = data1[3] #主資料2
    data4 = data1[4] #td2str 漲跌證券數合計
    title = data1[0] #標題
    date = data1[1] #日期
    data = process_data1(date=date,data=data2,data2=data3,td2str=data4,encodeing=big5)
    print(data)