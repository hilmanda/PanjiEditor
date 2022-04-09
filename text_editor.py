from tkinter import *
from button_action import Create_Btn
from tkinter.messagebox import showerror

class Text_area():
    def __init__(self, root, scroll):
        self.editor = Text(root, undo=True, font=("Lucida Console", 10), selectforeground="white", wrap='word', yscrollcommand=scroll.set)
        self.grid = self.editor.grid(row=0, column=1, sticky="nsew")
    def get_area(self):
        pass

class Text_scroll():
    def __init__(self, cursor_type):
        self.bar = Scrollbar(cursor=cursor_type)
        self.grid = self.bar.grid(row=0, column=2, sticky="nsew")

def Create_Editor(root):
    #create scrollbar
    scroll = Text_scroll("hand2")

    #create textbar
    txt = Text_area(root, scroll.bar) 

    #create button
    Create_Btn(root, txt.editor)

    #configure scrollbar
    scroll.bar.config(command=txt.editor.yview)

if __name__ == '__main__':
    showerror(title="Warning!", message="Run Main.py or Main.exe or PanjiEditor Shortcut to open the editor!")