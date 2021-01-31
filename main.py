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
from functools import partial

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

# select mode radio buttons
mode = tk.IntVar() # 1 = Go As Soon as Possible and 2 = Go later on

r1 = tk.Radiobutton(root,
               text="Go As Soon as Possible",
               padx = 20,
               variable=mode,
               value=1)
r1.config(font=('helvetica', 12))
r2 = tk.Radiobutton(root,
               text="Go later on",
               padx = 20,
               variable=mode,
               value=2)
r2.config(font=('helvetica', 12))

canvas1.create_window(830, 38, window=r1)
canvas1.create_window(785, 60, window=r2)

# current mode label
modeLabel = tk.Label(root, text='Current mode: Go as Soon As Possible')
modeLabel.config(font=('helvetica', 12))
canvas1.create_window(870, 85, window=modeLabel)

# enter address label + entry box
label2 = tk.Label(root, text='Enter your current address:')
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

d = tk.IntVar() # variable to store radio button day selection
def dayButtonClicked():
    print('day button clicked')
    print(str(d.get()))

def hoursButtonClicked(e1, e2):
    print('hours button clicked')
    print(e1.get())
    print(e2.get())

additionalComponents = []
def modeButtonClicked():
    if(mode.get() == 1):
        modeLabel['text'] = 'Current mode: Go as Soon As Possible' # change 'Current mode' label
        # clear any additional user input components
        for component in additionalComponents:
            try:
                canvas1.delete(component)
            except:
                component.destroy()

    else:
        modeLabel['text'] = 'Current mode: Go later on' # change 'Current mode' label

        # add additional user input components

        # select day radio buttons
        for x in range(7):

            day = ''
            if x == 0:
                day = 'Monday'
            elif x == 1:
                day = 'Tuesday'
            elif x == 2:
                day = 'Wednesday'
            elif x == 3:
                day = 'Thursday'
            elif x == 4:
                day = 'Friday'
            elif x == 5:
                day = 'Saturday'
            else:
                day = 'Sunday'

            r = tk.Radiobutton(root,
                                text=day,
                                padx=20,
                                variable=d,
                                value=x)
            r.config(font=('helvetica', 10))
            additionalComponents.append(r)

            canvas1.create_window(840, 115 + x*20, window=r)

        # set day button
        button1 = tk.Button(text='Set Day', command=dayButtonClicked, bg='grey', fg='white',
                            font=('helvetica', 10, 'bold'))
        additionalComponents.append(button1)
        canvas1.create_window(915, 120, window=button1)

        # selec time range text fields
        # enter address label + entry box
        lb = tk.Label(root, text='Enter earliest hour:')
        lb.config(font=('helvetica', 10))
        canvas1.create_window(1050, 150, window=lb)
        e1 = tk.Entry(root)
        canvas1.create_window(1150, 150, window=e1, width=30)
        additionalComponents.append(lb)
        additionalComponents.append(e1)

        # enter venue name label + entry box
        lb2 = tk.Label(root, text='Enter latest hour:')
        lb2.config(font=('helvetica', 10))
        canvas1.create_window(1050, 175, window=lb2)
        e2 = tk.Entry(root)
        canvas1.create_window(1150, 175, window=e2, width=30)
        additionalComponents.append(lb2)
        additionalComponents.append(e2)

        # 'Set hours' button
        button2 = tk.Button(text='Set Hours', command=partial(hoursButtonClicked, e1, e2), bg='grey', fg='white',
                            font=('helvetica', 10, 'bold'))
        additionalComponents.append(button2)
        canvas1.create_window(1100, 120, window=button2)


# function that is executed once the 'Get Safest Time' button is clicked
def buttonClicked():
    venue_name = entry2.get()

    print('clicked on button')
    print(venue_name)

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

    drawPlot([0,0,0,0,0,10,20,30,40,50,60,70,80,100,80,60,40,30,20,10,0,0,0,0], 0, 'Loblaws 1', '200 Earl Grey Dr, Ottawa, ON K2T 1B6')
    drawPlot([0,0,0,0,0,10,20,30,40,50,60,70,80,100,80,60,40,30,20,10,0,0,0,0], 150, 'Loblaws 2', 'Wall street, ON K2T 1B6')
    drawPlot([0, 0, 0, 0, 0, 10, 20, 30, 40, 50, 60, 70, 80, 100, 80, 60, 40, 30, 20, 10, 0, 0, 0, 0], 300, 'Loblaws 3', 'Area 51, Ottawa, ON K2T 1B6')
    drawPlot([0, 0, 0, 0, 0, 10, 20, 30, 40, 50, 60, 70, 80, 100, 80, 60, 40, 30, 20, 10, 0, 0, 0, 0], 450, 'Loblaws 4', 'Joe Mama')


guiComponents = []

def drawPlot(crowdValues, graphOffset, venueName, venueAddress):
    barOffset = 600
    counter = 1

    # draw venue name
    lb = tk.Label(root, text=venueName)
    lb.config(font=('helvetica', 20))
    guiComponents.append(lb)
    canvas1.create_window(100, graphOffset + 280, window=lb)

    # draw venue address
    lb = tk.Label(root, text='Address:  ')
    lb.config(font=('helvetica', 12))
    guiComponents.append(lb)
    canvas1.create_window(70, graphOffset + 310, window=lb)
    lb = tk.Label(root, text=venueAddress)
    lb.config(font=('helvetica', 12))
    guiComponents.append(lb)
    canvas1.create_window(300, graphOffset + 310, window=lb)

    # draw crowd bar graph
    for value in crowdValues:
        greenVal = int((value/100)*15)
        redVal = int(15 - greenVal)
        greenValHex = hex(greenVal)
        redValHex = hex(redVal)
        colorString = '#' + greenValHex[-1] + redValHex[-1] + "0"

        rectangle = canvas1.create_rectangle(barOffset, graphOffset+370, barOffset+20, graphOffset+370-value,outline="#000", fill=colorString)
        guiComponents.append(rectangle)

        lb = tk.Label(root, text=str(counter) + 'h')
        lb.config(font=('helvetica', 9))
        guiComponents.append(lb)
        canvas1.create_window(barOffset+10, graphOffset+390, window=lb)

        barOffset += 25
        counter += 1

def removePlots():
    for conponent in guiComponents:
        try:
            canvas1.delete(conponent)
        except:
            conponent.destroy()

# /////// Various Tkinter buttons ////////
# 'Get Safest Times' button
button1 = tk.Button(text='Get Safest Times', command=buttonClicked, bg='green', fg='white',
                    font=('helvetica', 15, 'bold'))
canvas1.create_window(350, 220, window=button1)

# 'Clear Data' button
button1 = tk.Button(text='Clear Data', command=removePlots, bg='red', fg='white',
                    font=('helvetica', 15, 'bold'))
canvas1.create_window(550, 220, window=button1)

# 'Set Mode' button
button1 = tk.Button(text='Set Mode', command=modeButtonClicked, bg='grey', fg='white',
                    font=('helvetica', 15, 'bold'))
canvas1.create_window(1000, 50, window=button1)

# enable the GUI main loop
print("got here")
root.mainloop()