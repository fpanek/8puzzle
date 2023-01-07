"""starts simple gui"""

#from Tkinter import *
from tkinter import *


def start_gui():
    root = Tk()
    choices = ['GB', 'MB', 'KB']
    variable = StringVar(root)
    variable.set('GB')

    w = OptionMenu(root, variable, *choices)
    w.pack();
    root.mainloop()