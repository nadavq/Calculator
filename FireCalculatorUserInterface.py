import tkinter
from tkinter.tix import Tk
from tkinter import *

class FireCalculatorUserInterface:

    def __init__(self):
        window = tkinter.Tk()
        window.geometry("400x600")
        window.title("Pro Calculator")
        self.__setFrames(window)
        window.mainloop()

    def __setFrames(self, window):
        output_frame = tkinter.Frame(window).pack()
        output_line = tkinter.Entry(output_frame, bd=5).pack()
