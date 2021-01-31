# Hackathon cuHacking:Snowed Nathaniel BG, James C, David S
# Team Name: Two Meter Apart
# Covid-19 Activity Planner

import json
import time
import requests
import TestConstants as con
import tkinter as tk
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from pandas import DataFrame
import venue as v

# /////// GUI SETUP ////////
# create window
from venue import venueInfo

root = tk.Tk()
canvas1 = tk.Canvas(root, width=1200, height=900, relief='raised')
canvas1.pack()

# title
label1 = tk.Label(root, text='Covid Activity Planner')
label1.config(font=('helvetica', 40))
canvas1.create_window(400, 50, window=label1)

# enter address label + entry box
label2 = tk.Label(root, text='Enter your city Name:')
label2.config(font=('helvetica', 12))
canvas1.create_window(100, 125, window=label2)
entry1 = tk.Entry(root)
canvas1.create_window(500, 125, window=entry1, width=550)

# enter venue name label + entry box
label2 = tk.Label(root, text='Enter venue name:')
label2.config(font=('helvetica', 12))
canvas1.create_window(72, 160, window=label2)
entry2 = tk.Entry(root)
canvas1.create_window(500, 160, window=entry2, width=550)

# draw other gui lines and shapes
canvas1.create_line(15, 100, 1180, 100)
canvas1.create_line(15, 250, 1180, 250)

# function that is executed once the 'Get Safest Visiting Times' button is clicked
def buttonClicked():

    venue_name = entry2.get()
    city_name = entry1.get()
    base = v.venueInfo()
    base.basicInfo(venue_name, city_name)

    print('clicked on button')
    print(base.name)
    print(base.city)


    # /////// Venue History ////////
    url = "https://besttime.app/api/v1/forecasts"

    params = {
        'api_key_private': con.BestTimeInfo.Api_Key_Private,
        'venue_name': con.venueInfo.venueName,
        'venue_address': con.venueInfo.venueAddress
    }

    response = requests.request("POST", url, params=params)
    data = json.loads(response.text)

    venueHistory1 = venueInfo()
    venueHistory1.addHistorical(data)
    venueHistory1.getRawDayData("Monday")

    drawPlot([0,0,0,0,0,10,20,30,40,50,60,70,80,100,80,60,40,30,20,10,0,0,0,0], 0, 'Loblaws 1', '200 Earl Grey Dr, Ottawa, ON K2T 1B6', 150, 8)
    drawPlot([0,0,0,0,0,10,20,30,40,50,60,70,80,100,80,60,40,30,20,10,0,0,0,0], 150, 'Loblaws 2', 'Wall street, ON K2T 1B6', 50, 6)
    drawPlot([0, 0, 0, 0, 0, 10, 20, 30, 40, 50, 60, 70, 80, 100, 80, 60, 40, 30, 20, 10, 0, 0, 0, 0], 300, 'Loblaws 3', 'Area 51, Ottawa, ON K2T 1B6', 100, 13)
    drawPlot([0, 0, 0, 0, 0, 10, 20, 30, 40, 50, 60, 70, 80, 100, 80, 60, 40, 30, 20, 10, 0, 0, 0, 0], 450, 'Loblaws 4', 'Joe Mama', 75, 23)


graphs = []

def drawPlot(crowdValues, graphOffset, venueName, venueAddress, rating, time):
    barOffset = 600
    counter = 1

    # draw venue name
    lb = tk.Label(root, text=venueName)
    lb.config(font=('helvetica', 20))
    canvas1.create_window(100, graphOffset + 280, window=lb)

    # draw venue address
    lb = tk.Label(root, text='Address:  ')
    lb.config(font=('helvetica', 12))
    canvas1.create_window(70, graphOffset + 310, window=lb)
    lb = tk.Label(root, text=venueAddress)
    lb.config(font=('helvetica', 12))
    canvas1.create_window(300, graphOffset + 310, window=lb)

    lb = tk.Label(root, text='live Rating: ' + str(rating), fg = 'red')
    lb.config(font=('helvetica', 12))
    canvas1.create_window(625, graphOffset + 280, window=lb)

    # draw crowd bar graph
    for value in crowdValues:
        if (counter == time):
            rectangle = canvas1.create_rectangle(barOffset, graphOffset + 370, barOffset + 20,
                                                 graphOffset + 370 - rating, outline="#000", fill="#f00")
            graphs.append(rectangle)

            lb = tk.Label(root, text=str(counter) + 'h')
            lb.config(font=('helvetica', 9))
            canvas1.create_window(barOffset + 10, graphOffset + 390, window=lb)

            barOffset += 25
            counter += 1

        else:
            rectangle = canvas1.create_rectangle(barOffset, graphOffset+370, barOffset+20, graphOffset+370-value,outline="#000", fill="#9cf")
            graphs.append(rectangle)

            lb = tk.Label(root, text=str(counter) + 'h')
            lb.config(font=('helvetica', 9))
            canvas1.create_window(barOffset+10, graphOffset+390, window=lb)

            barOffset += 25
            counter += 1

def removePlots():
    for bar in graphs:
        canvas1.delete(bar)



# 'Get Safest Visiting Times' button
button1 = tk.Button(text='Get Safest Visiting Times', command=buttonClicked, bg='green', fg='white',
                    font=('helvetica', 15, 'bold'))
canvas1.create_window(350, 220, window=button1)

# 'Get Safest Visiting Times' button
button1 = tk.Button(text='Clear Data', command=removePlots, bg='red', fg='white',
                    font=('helvetica', 15, 'bold'))
canvas1.create_window(550, 220, window=button1)

# enable the GUI main loop
root.mainloop()