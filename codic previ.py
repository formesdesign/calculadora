        self.display = ttk.Label(self, text="0", anchor=E, background=("black"), foreground=("white"), font="Arial 36", padding=(5,0,5,0)) #el pare d'esta label es def __init__(self):
        self.display.pack(side=TOP, fill=BOTH) #.pack empaqueta a la part de dalt, en este cas a d'alt
BOTONS EN PACK


        self.calcBttonC = ttk.Frame(self, width=68, height=50)
        btn = ttk.Button(self.calcBttonC, text="1", command=)
        self.calcBttonC.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)

        self.calcBttonC.pack(side=TOP)


                self.display.grid(column=0, row=0, columnspan=4) #.grid es per fer una graella

        self.calcBttonC = ttk.Frame(self, width=136, height=50)
        btn = ttk.Button(self.calcBttonC, text="C")
        self.calcBttonC.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        self.calcBttonC.grid(column=0, row=1, columnspan=2)

        self.calcBttonS = ttk.Frame(self, width=68, height=50)
        btn = ttk.Button(self.calcBttonS, text="S")
        self.calcBttonS.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        self.calcBttonS.grid(column=2, row=1)

