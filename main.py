# Hackathon cuHacking:Snowed Nathaniel BG, James C, David S
# Team Name: Two Meter Apart
# Covid-19 Activity Planner

# Import Libraries
# Import associations
import time
import TestConstants as con
import tkinter as tk
from bs4 import BeautifulSoup


# /////// GUI SETUP ////////
# create window
root = tk.Tk()
canvas1 = tk.Canvas(root, width=800, height=600, relief='raised')
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
entry1 = tk.Entry(root)
canvas1.create_window(500, 160, window=entry1, width=550)

# function that is executed once the 'Get Safest Visiting Times' button is clicked
def getSquareRoot():
    x1 = entry1.get()
    label3 = tk.Label(root, text='The Square Root of ' + x1 + ' is:', font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    label4 = tk.Label(root, text=float(x1) ** 0.5, font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)

# 'Get Safest Visiting Times' button
button1 = tk.Button(text='Get Safest Visiting Times', command=getSquareRoot, bg='brown', fg='white',
                    font=('helvetica', 15, 'bold'))
canvas1.create_window(400, 220, window=button1)

# enable the GUI main loop
root.mainloop()



