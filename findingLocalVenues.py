# Imports
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def getLocations(estaList, nameofplace, area):
    DRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver.exe')

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

    newnameofplace = nameofplace.replace(' ','+')
    newarea = area.replace(' ','+')
    newurl = 'https://www.google.com/maps/search/' + newnameofplace + '+' + newarea + '/'

    driver.get(newurl)

    name = []
    loc = []
    counter = 0
    while (name == [] and counter != 3):
        soup = bs(driver.page_source, 'html.parser')

        addresses = soup.find_all("div", {"class": "section-result-content"})

        for i in addresses:
            tempstring = str(i.find_next("h3", {"class": "section-result-title"}))
            templist, firstloc, secondloc = [], 0, 0

            for char in range(len(tempstring)):
                if tempstring[char] == '>':
                    firstloc = char
                elif tempstring[char] == '<':
                    secondloc = char
                    templist.append(tempstring[firstloc + 1:secondloc])
            name.append(templist[2])

            loc.append(str(i.find_next("span", {"class": "section-result-location"}))[86:-7])

        counter += 1

    if len(name) >= 1:
        estaList[0].basicInfo(name[0], loc[0])
    if len(name) >= 2:
        estaList[1].basicInfo(name[1], loc[1])
    if len(name) >= 3:
        estaList[2].basicInfo(name[2], loc[2])
    if len(name) >= 4:
        estaList[3].basicInfo(name[3], loc[3])
