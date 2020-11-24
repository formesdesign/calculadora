from tkinter import *
from tkinter import ttk

import calculator 

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculadora")

        self.display = calculator.Display(self) #aci estem cridant al display del document de la calculadora
        self.display.pack(side=TOP, fill=BOTH, expand=True) 

        self.teclado = calculator.Keyboard(self)
        self.teclado.pack(side=TOP) 



if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
