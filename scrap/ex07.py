import requests
from bs4 import BeautifulSoup
import re
import csv

url='https://finance.naver.com/sise/sise_quant.naver'
res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")
es = soup.find("table", attrs={'class':'type_2'}).find_all('tr')

file = open('data/코스피 지구숏치기', 'w', encoding='utf-8', newline="")
writer = csv.writer(file)
title = '삼성 인버스 2X 코스닥150 선물 ETN,"7,115'.split('')
writer.writerow(title)

for e in es:
    columns = e.find_all("td")
    if len(columns) <= 1:
        continue

    data = []
    for col in columns:
        col = col.get_text()
        col = re.sub('\n\t', '', col)
        data.append(col)  
    writer.writerow(data)    
    print(data)