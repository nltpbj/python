import requests
from bs4 import BeautifulSoup

#지구가 -100배 숏을 치고있어요
url = 'https://finance.naver.com/'
res = requests.get(url)

res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

es = soup.find('tbody', attrs={'id':'_topItems1'}).find_all('tr', limit=5)
for e in es:
    title = e.find('a').get_text()
    td = e.find_all('td')
    price = td[0].get_text()
    updown = td[1].get_text()
    rate = td[2].get_text()
    print(title, price, updown, rate.strip())