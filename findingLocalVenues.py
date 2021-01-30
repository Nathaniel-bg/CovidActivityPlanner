#Imports
from bs4 import BeautifulSoup as bs
import requests as rq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

def getLocations():
    DRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),'chromedriver.exe')

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

    driver.get('https://www.google.com/maps/search/loblaws+toronto/')
    time.sleep(0.2)
    #response = rq.get('https://www.google.com/maps/search/loblaws+toronto/')
    #response = rq.get('https://realpython.com/python-requests/')

    soup = bs(driver.page_source,'html.parser')

    #addresses = soup.find_all('span')
    addresses = soup.find_all("div",{"class" : "section-result-content"})
    #location = addresses.find_next('span','class=section-result-location)
    #ye = addresses.find_next('span','jsan:"7.section-result-location')

    for i in addresses:
        name = str(i.find_next("span", {"jstcache": "130"}))
        loc = i.find_all("span", {"class": "section-result-location"})
        locList = []
        for j in loc:
            locList.append(j)
        print(name, locList)



getLocations()