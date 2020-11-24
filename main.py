from tkinter import *
from tkinter import ttk

import calculator 

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculadora")

        self.display = calculator.Display(self) #aci estem cridant al display del document de la calculadora
        self.display.pack(side=TOP, fill=BOTH, expand=True) 

        self.teclado = ttk.Frame(self, width=calculator.WIDTH*4, height=calculator.HEIGHT*5)
        self.teclado.grid_propagate(0)
        self.teclado.pack(side=TOP, fill=BOTH, expand=True) 

        #ara podem crear els botons dins una grida
        botonC = calculator.CalcButton(self.teclado, "C")
        botonC.grid(row=0, column=0)

        botonM = calculator.CalcButton(self.teclado, "+/-")
        botonM.grid(row=0, column=1)
        
        botonP = calculator.CalcButton(self.teclado, "%")
        botonP.grid(row=0, column=2)

        botonD = calculator.CalcButton(self.teclado, "÷")
        botonD.grid(row=0, column=3)

        boton7 = calculator.CalcButton(self.teclado, "7")
        boton7.grid(row=1, column=0)

        boton8 = calculator.CalcButton(self.teclado, "8")
        boton8.grid(row=1, column=1)

        boton9 = calculator.CalcButton(self.teclado, "9")
        boton9.grid(row=1, column=2)

        botonX = calculator.CalcButton(self.teclado, "x")
        botonX.grid(row=1, column=3)

        boton4 = calculator.CalcButton(self.teclado, "4")
        boton4.grid(row=2, column=0)
        
        boton5 = calculator.CalcButton(self.teclado, "5")
        boton5.grid(row=2, column=1)
        
        boton6 = calculator.CalcButton(self.teclado, "6")
        boton6.grid(row=2, column=2)
        
        botonMN = calculator.CalcButton(self.teclado, "-")
        botonMN.grid(row=2, column=3)

        boton1 = calculator.CalcButton(self.teclado, "1")
        boton1.grid(row=3, column=0)
        
        boton2 = calculator.CalcButton(self.teclado, "2")
        boton2.grid(row=3, column=1)
        
        boton3 = calculator.CalcButton(self.teclado, "3")
        boton3.grid(row=3, column=2)
        
        botonMS = calculator.CalcButton(self.teclado, "+")
        botonMS.grid(row=3, column=3)

        boton0 = calculator.CalcButton(self.teclado, "0")
        boton0.grid(row=4, column=0, columnspan=2)
        
        botonCm = calculator.CalcButton(self.teclado, ",")
        botonCm.grid(row=4, column=2)
        
        botonI = calculator.CalcButton(self.teclado, "=")
        botonI.grid(row=4, column=3)




        #intentar montar un for amb una llibretria

"""
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

"""




if __name__ == "__main__":
    app = MainApp()
    app.mainloop()