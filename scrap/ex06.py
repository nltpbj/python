import requests
from bs4 import BeautifulSoup

def create_soupo(query):
    url=''
    headers={
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
        }
    res = requests.get(url, headder=headers)
    soup = BeautifulSoup(res.text, 'lxm')
    return soup

 