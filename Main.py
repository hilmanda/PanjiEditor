from tkinter import *
from window import *
from text_editor import *

def start():
    #creat objek window
    root = Window()
    
    #create editor area and scrollbar
    Create_Editor(root)

    #deploy to screen
    root.mainloop()

if __name__ == '__main__' :
    start()