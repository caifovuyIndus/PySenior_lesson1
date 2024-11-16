print(f'lesson9\n')
import requests
from bs4 import BeautifulSoup

data_site = requests.get('https://coinmarketcap.com/')
print('site coin market status code', data_site.status_code)

if data_site.status_code == 200:
    print('coin market is connected')
    soup = BeautifulSoup(data_site.text, features='html.parser')
    soup_list = soup.find_all('div', {'class': 'sc-b3fc6b7-0 dzgUIj'})

    for block in soup_list:
        print('parse result', block)