from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import json
import csv

def wait_until(browser, xpath):
  WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

def create_soup(query):
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')
  options.add_experimental_option('detach', True)
  browser = webdriver.Chrome(options=options)
  browser.maximize_window()

  url='https://www.gmarket.co.kr/n/search?keyword={}'.format(query)
  browser.get(url)

  prev_height = browser.execute_script('return document.body.scrollHeight')
  while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if prev_height == curr_height:
      print('스크롤완료!')
      break
    prev_height = curr_height

  soup = BeautifulSoup(browser.page_source, 'lxml')
  browser.quit()
  return soup

def search(query):
  soup = create_soup(query)
  file = open(f'data/{query}.csv','w', encoding='utf-8-sig', newline="")
  writer = csv.writer(file)
  title='title,price,image,link'.split(',')
  writer.writerow(title)

  es = soup.find_all('div', attrs={'class':re.compile('^box__item-container')})
  for e in es:
    title = e.find('span', attrs={'class':'text__item'}).get_text()
    price = e.find('strong', attrs={'class':'text text__value'}).get_text()
    image = 'http:' + e.find('img')['src']
    link = e.find('a')['href']
    print(title)
    print(price)
    print(image)
    print(link)
    print('-' * 50)
    #item = {'title':title, 'price':price, 'image':image, 'link':link}
    #items.append(item)
    #json_data=json.dumps(items, indent=4, ensure_ascii=False)
    data=[title, price, image, link]
    writer.writerow(data)
  return 'success'

query='자전거'
print(search(query))