from tkinter import *


def start_gui():
    """
    Starts a simple GUI.
    :return: none
    """
    root = Tk()
    choices = ['GB', 'MB', 'KB']
    variable = StringVar(root)
    variable.set('GB')

    w = OptionMenu(root, variable, *choices)
    w.pack()
    root.mainloop()
