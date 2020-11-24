from tkinter import *
from tkinter import ttk

#son les celdes de les nostra tabla que hem determinat per fer la calculador
WIDTH = 68
HEIGHT = 50

class Display(ttk.Frame):
    def __init__(self, parent): #parent penja de main
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT)
        self.pack_propagate(0) #es lo mateix 0 o ficar false
        s = ttk.Style() 
        s.theme_use("alt")

        self.label = ttk.Label(self, text="0", anchor=E, background=("black"), foreground=("white"), font="Arial 36") #el pare d'esta label es def __init__(self):)
        self.label.pack(side=TOP, fill=BOTH, expand=True)


class CalcButton(ttk.Frame):
    def __init__(self, parent, text, command=None, width=1, height=1):
        ttk.Frame.__init__(self, parent, width=WIDTH*width, height=HEIGHT*height)
        self.pack_propagate(0)
        s = ttk.Style() 
        s.theme_use("alt")

        ttk.Button(self, text=text, command=command).pack(side=TOP, fill=BOTH, expand=True)
        # este self penja del CalcButton, creo un botó i el peguem a mi mateix amb el parent
        
