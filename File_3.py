import matplotlib
import pandas as pd
import quandl, datetime
import numpy as np
from sklearn import model_selection,neighbors,svm
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import math
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
import yfinance as yf
import tkinter as tk
from pandas_datareader import data
import urllib
import json
import  math
import quandl
LARGE_FONT=("Verdana",12)
NORMAL_FONT=("Verdana",10)
SMALL_FONT=("Verdana",8)
from tkinter import  ttk
style.use("ggplot")

f=Figure()
a=f.add_subplot(111)


#a.plot([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9])


def changeExchange(toWhat,pn):


def popupmsg(ms):

    popup=tk.Tk()
    popup.wm_title("!")
    label=ttk.Label(popup,text=msg,font=NORMAL_FONT)
    label.pack(side="top",fill="x",pady=10)
    B1=ttk.Button(popup,text="okay",command=popup.destroy())
    B1.pack()
    popup.mainloop()

def animate(i):
    df=pd.read_csv("WIKI-FB.csv")
    df=pd.DataFrame(df)
    x=np.array(df['Close'],df['Adj. High'])
    y=np.array(df['Date'])
    a.plot(y,x)
    a.set_title("Set title")


class SeaofBTCapp(tk.Tk):

    def __init__(self,*args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
#__init__ Immediately occurs at a priority. Self is not necessary but good to add.
#*args: Add any number of variables
#**Kwargs: Add any number of dictionary you wanna
        container=tk.Frame(self)

        container.pack(side="top",fill="both",expand=True)
#Fill: Fill the space alloted the pack
#expand: Expand if there's space
        container.grid_rowconfigure(0,weight=1)# 0 is minimum size.Weight is priority
        container.grid_columnconfigure(0,weight=1)

        menubar=tk.Menu(container)
        filemenu=tk.Menu(menubar,tearoff=0)
        filemenu.add_command(label="Save settings",command=lambda : popupmsg("Not supported just yet"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=quit)
        menubar.add_cascade(label="File",menu=filemenu)

        exchangeChoice=tk.Menu(menubar,tearoff=1)
        exchangeChoice.add_command(label="EUR/USD",command=lambda :changeExchange("BTCE_Display name1","tickersymbol"))
        exchangeChoice.add_command(label="GBP/USD",command=lambda :changeExchange("BTCE_Display name2","tickersymbol"))
        exchangeChoice.add_command(label="CHF/USD",command=lambda :changeExchange("BTCE_Display name3","tickersymbol"))
        exchangeChoice.add_command(label="CHF/EUR",command=lambda :changeExchange("BTCE_Display name4","tickersymbol"))


        tk.Tk.config(self,menu=menubar)

        self.frames ={} #Add pages here in for loopOne application that loads different windows

        for F in (StartPage, PageOne):
            frame = F(container,self)

            self.frames[F]=frame

            frame.grid(row=0,column=0,sticky ="nsew")
#grid or pack. Grid. What grid or column wanna
#sticky: Alignment + Stretch. Sticky to north,east,....nsew: everything to size of that window
        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise() #bring to front

class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Start Page",font=LARGE_FONT) #Label. Returing this stuff.Created an object
        label.pack(pady=10,padx=10)
        button1=tk.Button(self,text="Visit Page 1",
                          command=lambda : controller.show_frame(PageOne)) #Command: Works with function on load. If pass a string, won't work
        button1.pack()


class PageOne(tk.Frame):
   def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="A",font=LARGE_FONT) #Label. Returing this stuff.Created an object
        label.pack(pady=10,padx=10)
        button2=tk.Button(self,text="Back to home",
                          command=lambda : controller.show_frame(StartPage)) #Command: Works with function on load. If pass a string, won't work
        button2.pack()

        canvas=FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        toolbar=NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)


app=SeaofBTCapp()
app.geometry("480x320")
ani=animation.FuncAnimation(f,animate,interval=1000000) #1000=1ms
app.mainloop()



