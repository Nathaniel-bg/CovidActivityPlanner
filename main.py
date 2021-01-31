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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame


# /////// GUI SETUP ////////
# create window
from venue_history import VenueHistory

root = tk.Tk()
canvas1 = tk.Canvas(root, width=1200, height=300, relief='raised')
canvas1.pack()

# title
label1 = tk.Label(root, text='Covid Activity Planner')
label1.config(font=('helvetica', 40))
canvas1.create_window(400, 50, window=label1)

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


# function that is executed once the 'Get Safest Visiting Times' button is clicked
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

    venueHistory1 = VenueHistory(data)
    venueHistory1.getRawDayData("Monday")

    drawPlot('Time', ['2', '4', '6', '8', '10', '12', '14'], 'Crowd', [15, 20, 21, 100, 200, 20, 20])
    drawPlot('Time', ['2', '4', '6', '8', '10', '12', '14'], 'Crowd', [15, 20, 21, 100, 200, 20, 20])
    drawPlot('Time', ['2', '4', '6', '8', '10', '12', '14'], 'Crowd', [15, 20, 21, 100, 200, 20, 20])
    drawPlot('Time', ['2', '4', '6', '8', '10', '12', '14'], 'Crowd', [15, 20, 21, 100, 200, 20, 20])
    drawPlot('Time', ['2', '4', '6', '8', '10', '12', '14'], 'Crowd', [15, 20, 21, 100, 200, 20, 20])
    label3 = tk.Label(root, text='Enter your current address:')
    label3.config(font=('helvetica', 12))
    canvas1.create_window(1, 1, window=label3)


def drawPlot(xName, xValues, yName, yValues):
    data1 = {
        xName: xValues,
        yName: yValues
    }
    df1 = DataFrame(data1, columns=[xName, yName])
    figure1 = plt.Figure(figsize=(5, 6), dpi=50)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.X)
    df1 = df1[[xName, yName]]
    df1.plot(kind='bar', legend=True, ax=ax1, fontsize=20)
    ax1.set_title('', fontsize=25)


# 'Get Safest Visiting Times' button
button1 = tk.Button(text='Get Safest Visiting Times', command=buttonClicked, bg='brown', fg='white',
                    font=('helvetica', 15, 'bold'))
canvas1.create_window(400, 220, window=button1)

# enable the GUI main loop
root.mainloop()



