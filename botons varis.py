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
    def __init__(self, parent, text, command=None, width=1, height=1): #ho fiquem xq quan volem fer mes amplada, informarem el boto al main
        ttk.Frame.__init__(self, parent, width=WIDTH*width, height=HEIGHT*height)
        self.pack_propagate(0)
        s = ttk.Style() 
        s.theme_use("alt")

        ttk.Button(self, text=text, command=command).pack(side=TOP, fill=BOTH, expand=True)
        # este self penja del CalcButton, creo un botó i el peguem a mi mateix amb el parent


botones = (('C', 1), ('+/-',1), ('%',1), ('÷', 1), ('7', 1), ('8', 1), ('9', 1), ('x', 1), ('4', 1), ('5', 1), ('6', 1), ('-', 1), ('1', 1), ('2', 1), ('3', 1), ('+', 1), ('0',2), (',', 1), ('=', 1))
coordenadas = []

class Keyboard(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*5)
        self.pack_propagate(0)
        s = ttk.Style() 
        s.theme_use("alt")

        coordenadas = []
        for fila in range (5):
            for columna in range (4):
                coordenadas.append ((fila, columna))

        k = 0
        for tecla, ancho in botones:
            boton = CalcButton(self, tecla, width=ancho)
            boton.grid(row=coordenadas [k][0], column=coordenadas [k][1], columnspan=ancho)

            k += ancho 

dbotones = [
    {
        'text': 'C',
        'r': 0,
        'c': 1,
    },
    {
        'text': '+/-',
        'r': 0,
        'c': 2,
    },
    {
        'text': '÷',
        'r': 0,
        'c': 3,
    },
    {
        'text': '7',
        'r': 1,
        'c': 0,
    },
    {
        'text': '8',
        'r': 1,
        'c': 1,
    },
    {
        'text': '9',
        'r': 1,
        'c': 2,
    },
    {
        'text': 'x',
        'r': 1,
        'c': 3,
    },
    {
        'text': '4',
        'r': 2,
        'c': 0,
    },
    {
        'text': '5',
        'r': 2,
        'c': 1,
    },
    {
        'text': '6',
        'r': 2,
        'c': 2,
    },
    {
        'text': '-',
        'r': 2,
        'c': 3,
    },
    {
        'text': '1',
        'r': 3,
        'c': 0,
    },
    {
        'text': '2',
        'r': 3,
        'c': 1,
    },
    {
        'text': '3',
        'r': 3,
        'c': 2,
    },
    {
        'text': '+',
        'r': 3,
        'c': 3,
    },
    {
        'text':'0',
        'r':4,
        'c':0,
        'w': 2
    },
    {
        'text': ',',
        'r': 4,
        'c': 2,
    },
    {
        'text': '=',
        'r': 4,
        'c': 3,
    },
]
class Keyboard_amb_DIC(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*5)
        self.pack_propagate(0)
        s = ttk.Style() 
        s.theme_use("alt")

        for boton in dbotones:
            w = boton.get ("w", 1)
            h = boton.get ("h", 1)

            btn = CalcButton(self, boton ["text"], widh=w, height=h)
            btn.grid(row=boton["r"], column=boton["c"], columnspan=w, rowspan=h)

