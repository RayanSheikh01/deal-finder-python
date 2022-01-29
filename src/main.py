
from web_scraper import returnXML 
import pandas as pd
import find_details_amazon as find_amazon
from notifypy import Notify
import schedule
import time

# ADD this if needed --> job is the main program which will be run daily at 12pm
# def job():
# read products.csv file and products_history.csv file
products_history = pd.read_csv('./products_history.csv', sep=",", index_col='number')
old_prices = products_history.price
products = pd.read_csv('./products.csv', sep=",", index_col='number')
links = products['link']

# Webscrape user-inputted link
for link in links:
    # get index of row of link in csv file and assign to variable index
    index = products.index[products['link']==link][0]
    old_price_index = products_history.index[products['link']==link][0]
    soup = returnXML(link)

    # below try-except statements will try to get price, title and rating of products
    price = "NA"
    try:
        price = find_amazon.findPrice(soup)
        
        # if the price is not found
    except AttributeError:
        count = 0
        # sometimes price is None even if there is an element therefore loop makes sure that if there
        # is a element with the same id then it will be caught
        while count < 3 and price is None:
            price = find_amazon.findPrice(soup)
            count += 1
    # if the new price is cheaper than the old price
    if float(price) < float(products_history.loc[old_price_index, 'price']):
        notification = Notify()
        notification.title = "Price cut on {}".format(products.loc[index, 'title'])
        notification.message = "Price cut!"
        notification.send()
            

    try:
        title = find_amazon.findTitle(soup).strip()
        

    except AttributeError:
        title ="NA"

    try:
        rating = find_amazon.findRating(soup)

    except AttributeError:
        rating = "NA"


    products.loc[index, 'title'] = title
    products.loc[index, 'price'] = price
    products.loc[index, 'rating'] = rating
    products.to_csv("products.csv")
    products.to_csv("products_history.csv")

# Add this if using schedule module
# schedule.every().day.at("12:00").do(job)    #change the schedule of program execution here

# ADD this if using schedule module 
# while True: #check if the job is waiting to be run or not every 30s
#    schedule.run_pending()
#    time.sleep(30) #change 30 to another number if you want to check at a faster rate
