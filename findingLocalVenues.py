#Imports
from bs4 import BeautifulSoup as bs
import requests as rq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

DRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),'chromedriver.exe')

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get('https://www.google.com/maps/search/loblaws+toronto/')
time.sleep(5)
#response = rq.get('https://www.google.com/maps/search/loblaws+toronto/')
#response = rq.get('https://realpython.com/python-requests/')

soup = bs(driver.page_source,'html.parser')

addresses = soup.find_all('span')
#addresses = soup.find("div",{"class" : "section-result-details-container"})
#ye = addresses.find_next('span','jsan:"7.section-result-location')
print(addresses)