# Imports
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import venue


def getLocations(estaList, name, area):
    DRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver.exe')

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

    driver.get('https://www.google.com/maps/search/canadian+tire+kanata/')

    name = []
    loc = []
    while name == []:
        soup = bs(driver.page_source, 'html.parser')

        addresses = soup.find_all("div", {"class": "section-result-content"})

        for i in addresses:
            name.append(str(i.find_next("span", {"jstcache": "130"}))[21:-7])
            loc.append(str(i.find_next("span", {"class": "section-result-location"}))[86:-7])

    if len(estaList) >= 1:
        estaList[0].basicInfo(name[0], loc[0])
    if len(estaList) >= 2:
        estaList[1].basicInfo(name[1], loc[1])
    if len(estaList) >= 3:
        estaList[2].basicInfo(name[2], loc[2])
    if len(estaList) >= 4:
        estaList[3].basicInfo(name[3], loc[3])
