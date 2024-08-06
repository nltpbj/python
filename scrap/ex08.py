import requests
from bs4 import BeautifulSoup
import re
import csv

def create_soup(page):
    url='https://finance.naver.com/sise/sise_quant.naver'
    res= requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

for i in range(1, 3):
    soup = create_soup(i)
    colunms = soup.find('table', attrs={'class':'type_2'}).find_all('tr')
    if len(colunms) <= 1:
        continue
    data = [re.sub('\n|\t|상승|하락|보합','',col.get_text()) for col in colunms]