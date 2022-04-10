from tkinter import *
from tkinter.messagebox import showerror
from os import path

class Window(Tk):
    #create and configure window
    def __init__(self):
        super().__init__()
        self.title('PanjiEditor - Untitled')
        imgpath = path.dirname(__file__)
        self.iconphoto(True, PhotoImage(file= imgpath + '/icons/favicon-32.png'))
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, minsize=800, weight=1)
        self.minsize(height=800, width=885)

if __name__ == '__main__':
    showerror(title="Warning!", message="Run Main.py or Main.exe or PanjiEditor Shortcut to open the editor!")