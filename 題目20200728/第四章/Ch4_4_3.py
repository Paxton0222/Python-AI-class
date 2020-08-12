import requests

url = "https://www.googleapis.com/books/v1/volumes"

url_params = {'q': 'Python',
              'maxResults': 5, 
              'projection': 'lite'}
r = requests.get(url, params=url_params) #向googleapis傳送請求
print(r.json()) #回傳所有 Python 書籍的名稱和各項資料