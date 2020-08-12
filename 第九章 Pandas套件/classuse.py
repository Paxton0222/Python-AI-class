from pandas import read_csv
import requests,sys,string
import pandas as pd
from bs4 import BeautifulSoup

class Getdata():
    def requests_html(url,headers):
        r = requests.get(url,headers=headers)
        return r.text
    
    def requests_binary(url):
        r = requests.get(url)
        return r.content
    
    def download_binary(url,title):
        html = Getdata.requests_binary(url)
        with open('{title}'.format(title=title),'wb')as f:
            data = f.wrtie(html)
            f.close()
        return "{title} done!".format(title=title)
    
    def download_html(url,title,mode,encoding):
        html = Getdata.requests_html(url)
        with open('{title}'.format(title=title),mode=mode,encoding=encoding)as f:
            f.write(html)
            f.close()
        return "{title} done!".format(title=title)
    
    def process_html(html,mode):
        data = BeautifulSoup(html,mode)
        return data
    
    def dl_csv_html(url,headers):
        html = Getdata.requests_html(url,headers)
        data = Getdata.process_html(html,'lxml')
        title = data.find('title')
        data = data.find_all('body')
        data_title = data[0].find('th').div.string #109年07月 發行量加權股價報酬指數
        data = data[0].find_all('td') 
        #print(data_title)
        #print(len(data))
        list1 = []
        for i in data:
            data = i.string
            list1.append(data)
        #print(type(list1))
        date = list1[0]
        i = 2
        x = 3
        #------------------data----------------------
        date = str(date).replace("\u3000","") #日期
        title = list1[1] #發行量加權股價報酬指數
        data_date_list = [] #年月日
        data_list = [] #主要資料
        while i<len(list1):
            data_date = list1[i]
            i+=2
            data_date_list.append(data_date)
        while x<len(list1):
            data = list1[x]
            x+=2
            data_list.append(data) 
        #------------to csv--------------
        dict1 = {date:data_date_list,title:data_list}
        df = pd.DataFrame(dict1)
        df.to_csv('{}.csv'.format(data_title),index=False,encoding='big5')
        with open('{}.csv'.format(data_title),'r+',encoding='big5')as f:
            read = f.read()
            f.seek(0,0)
            f.write(data_title+'\n'+read)
            f.close()
        #------------to html-------------
        df = read_csv('{}.csv'.format(data_title),encoding='big5')
        print(df)
        df.to_html('{}.html'.format(data_title))
        print("{t}.csv檔 和 {t}.html檔 下載完成!".format(t=data_title))