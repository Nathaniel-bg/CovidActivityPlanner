#imports
import requests as rq
import json
import tkinter
import bs4

#user inputs
def userInput():
    #userInfo = [input("Address "), input("City "), input("Province/State "), input("Venue ")]
    userInfo = ['Potato Dr','Ottawa','Ontario','Superstore']
    return userInfo

#_______________________TEST_HERE___________________________
test = userInput()
for i in test:
    print(i)