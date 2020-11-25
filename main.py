from tkinter import *
from tkinter import ttk

import calculator 

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculadora")

        self.calculator = calculator.Calculator(self) #aci estem cridant al display del document de la calculadora

if __name__ == '__main__':
    app = MainApp()
    app.mainloop()