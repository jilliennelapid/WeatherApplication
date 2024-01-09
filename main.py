from model import Model
from view import View
from controller import Controller
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")

        model = Model()
        view = View(self)
        controller = Controller(model, view)

        view.grid(row=0, column=0, padx=10, pady=10)

        View.set_controller(view, controller)



if __name__ == '__main__':
    # Creates an object from class App, which also creates the window using tkinter module
    app = App()
    app.mainloop()