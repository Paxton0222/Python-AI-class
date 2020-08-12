import sys
sys.path.append('./classuse.py')
from classuse import Getdata

date = input('請輸入日期(年/月/日):')
#date = "20200610"
url = "https://www.twse.com.tw/indicesReport/MFI94U?response=html&date={}".format(date)
title = 'test.html'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
#https://www.twse.com.tw/indicesReport/MFI94U?response=html&date=20200710

if __name__ == "__main__":
    #html = Getdata.download_html(url,title,mode='w',encoding='utf8')
    #print(html)
    Getdata.dl_csv_html(url,headers)