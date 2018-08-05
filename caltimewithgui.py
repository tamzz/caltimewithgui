# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 18:18:43 2018

@author: tammy_000
"""

import tkinter
from tkinter import Entry


# a function that contain 2 function
def foo():
    popupmsg()
   # timecauseu()

def timecauseu(wage,twkhr,spent):
    
    
    earnperhr = wage/twkhr
    ttimecostu = spent/earnperhr
    return (ttimecostu)
    print(ttimecostu)
   
    
    
#function to create a new pop up window
def popupmsg():
    popup = tkinter.Tk()
    popup.wm_title("!")
    # get the text from the previous pop up window
    #remember to convert to int
    getstring = Wageentry.get()
    getint = int(getstring)
    
    getstring = Wkhrentry.get()
    getint2 = int(getstring)
    
    getstring = expenseentry.get()
    getint3 = int(getstring)
     
    NORM_FONT = ("Helvetica", 10)
    label = tkinter.Label(popup, text=getstring, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    
    result = timecauseu(getint,getint2,getint3)
    label2 = tkinter.Label(popup, text=result, font=NORM_FONT)
    label2.pack(side="top", fill="x", pady=10)
    
    
    
    B1 = tkinter.Button(popup, text="close", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
    
    
#open a new pop up window
newwindow = tkinter.Tk()

#Wage
Wage = tkinter.Label(newwindow, text="Monthly Wage")
Wage.pack(side="top", fill="x", pady=10)
#create a new entery box
Wageentry  = Entry(newwindow)
Wageentry.pack()

#Monthly working hr
Wkhr = tkinter.Label(newwindow, text="Monthly working hr")
Wkhr.pack(side="top", fill="x", pady=10)
#create a new entery box
Wkhrentry  = Entry(newwindow)
Wkhrentry.pack()

#Total expense
expense = tkinter.Label(newwindow, text=" Monthly expense")
expense.pack(side="top", fill="x", pady=10)


#create a new entery box
expenseentry  = Entry(newwindow)
expenseentry.pack()

btn = tkinter.Button(newwindow ,text= "textbtn",command = foo)
btn.pack()
newwindow .mainloop()

