import requests
from bs4 import BeautifulSoup
import re

def craete_soup(query, page):
    url = "https://www.coupang.com/np/search?q={}&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=\
        false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(query, page)
    headers = { 
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    return soup
itmes=[]
index = 0
for i in range(1, 6):
    soup = craete_soup('노트북', i)
    es = soup.find_all('li', attrs={'class':re.compile('^search-product')})
    for e in es:
        name = e.find('div', attrs={'class':'name'})
        if name:
            name = name.get_text().strip()
        else:
            continue
        price = e.find('strong', attrs={"class":"price-value"})
        if price:
            price = price.get_text()
        else:
            continue
        image = e.find('img', attrs={'class':'search-product-wrap-img'})
        if image:
            image = 'http:' + image['src']
        else:
            continue

        index +=1
        print(index, name)
        print('price:', price)
        print('image:', image)

        item = {'name':name, 'price':price, 'image':image}
        itmes.append(item)
        #res_image = requests .get(image)
        #with open('images/img{}.jpg'.format(index), 'wb') as file:
           #file.write(res_image.content)



import json
with open('data/shop.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(itmes, indent=4, sort_keys=True, ensure_ascii=True))

print('상품수:', index)