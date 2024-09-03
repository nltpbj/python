from selenium import webdriver
import time
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.maximize_window()

query='김기인'
url='https://www.google.com/search?sca_esv=0938baf10882972d&sxsrf=ADLYWIKsAsg0yo_Yejo7qMw9R7cMyOPstg:1722991564149&q={}&udm=2&fbs=AEQNm0DmKhoYsBCHazhZSCWuALW8l8eUs1i3TeMYPF4tXSfZ98Z_XVxzNb13fp2atSe3aTZxh00P4RN46vKaeCU6lCwgokKSAjPDH2MlsSy-8gaDDUQaKgJ6WGNN_FX8vJhn-4awYk5Gk7BAEdii98OBeClKK9JjFHF7liK4K3tHwCkeIdyWNQJGJEedbu5ErfKv3dVRvt_95CfohgWcKP7_C0Z4J1v1EA&sa=X&ved=2ahUKEwjZgYfh0-GHAxXhiK8BHVaXE10QtKgLegQIDxAB&biw=1680&bih=892&dpr=1'.format(query)
browser.get(url)

prev_height = browser.execute_script('return document.body.scrollHeight')
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if prev_height == curr_height:
        print('스크롤완료')
        break
    prev_height = curr_height

from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.text, 'lxml')

with open('data/image.html', 'w', encoding='utf-8') as file:
  file.write(soup.prettify())

es = soup.find_all('div', attrs={'class':re.compile('^eA0Zlc')})
print(len(es))

for index, e in enumerate(es):
  title = e.find('div', attrs={'class':'toI8Rb OSrXXb'})
  image = e.find('img')['src']
  print(index+1, title.get_text())
  print(image)
  print('-' * 50)