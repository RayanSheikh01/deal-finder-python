import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
def returnXML(URL):
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'lxml')

    return soup
    

