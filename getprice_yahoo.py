import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/EURUSD%3DX?p=EURUSD%3DX"

# ارسال درخواست به سایت
response = requests.get(url)

# خواندن محتوای صفحه با استفاده از BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# پیدا کردن المان مربوط به قیمت لحظه‌ای EUR/USD
price = soup.find('fin-streamer',{'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'})

# چاپ قیمت لحظه‌ای
print(price.text)
