# imports
import requests as rq
import json
import tkinter
import bs4
import findingLocalVenues as flv
import venue

# user inputs
def userInput():
    #userInfo = [input("Address "), input("City "), input("Province/State "), input("Venue ")]
    userInfo = ['Potato Drive','Ottawa','Ontario','Superstore']
    return userInfo

# _______________________TEST_HERE___________________________
def test(estaList):
    test = flv.getLocations(estaList,'Canadian tire', 'east toronto')

establishment_01 = venue.venueInfo()
establishment_02 = venue.venueInfo()
establishment_03 = venue.venueInfo()
establishment_04 = venue.venueInfo()

estaList = [establishment_01, establishment_02, establishment_03, establishment_04]
test(estaList)

print(estaList[0].name, estaList[0].address)
print(estaList[1].name, estaList[1].address)
print(estaList[2].name, estaList[2].address)
print(estaList[3].name, estaList[3].address)