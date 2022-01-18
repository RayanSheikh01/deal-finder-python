
import re
from bs4 import BeautifulSoup
import time

def findPrice(soup):
    # Find the <div> where price is and then find the price however there are two price attributes hence
    # the regex (priceText = £xy.xy£xy.xy prior to regex search)
    # sleep time added so all elements in product page can fully load 
    #time.sleep(3)
    price = soup.find("span", attrs={"class": 'a-offscreen'})
    price = price.text
    price = price[1:]
    # price after regex search is an object hence it is grouped at the first object (object 0)
    #price = re.search("\d+\.\d{1,2}", price)
    return price

def findTitle(soup):
    title = soup.find("span", attrs={"id": 'productTitle'}).text
    return title

def findRating(soup):
    rating = re.search("\d\.\d{1,2}",soup.find("span", attrs={"class": 'a-icon-alt'}).text).group(0)
    return rating