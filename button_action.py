from tkinter import *
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfile, asksaveasfile

class Button_action():
    def __init__(self, root, txt_edit):
        self.__filename = None
        self.__root = root
        self.__text = txt_edit

    #open a file method
    def open_file(self):
        file = askopenfile(mode='r')
        self.__filename = file.name
        text = file.read()
        self.__text.delete(0.0, END)
        self.__text.insert(0.0, text)

        self.__root.title(f'PanjiEditor - {self.__filename}')

    #save file method
    def save_file(self):
        file = asksaveasfile(defaultextension="txt", filetypes=[("Text Files", ".txt"), ("All Files", ".*")],)
        self.__filename = file.name
        text = self.__text.get(1.0, END)
        file.write(text)

        self.__root.title(f"PanjiEditor - {self.__filename}")

class Btn():
    def __init__(self, frame, text, command, row=0, column=0, cursor = "hand2", relief=None, sticky = "ew", padx = 0, pady = 0):
        self.__btn = Button(frame, text=text, cursor=cursor, relief=relief, bd=2, command=command)
        self.__grid = self.__btn.grid(row=row, column=column, sticky=sticky, padx=padx, pady=pady)

    def get_grid(self):
        return self.__grid

    def btn(self):
        return self.__btn

def Create_Btn(root, txt_editor):

    btnObj = Button_action(root, txt_editor)

    #create button frame
    frm_buttons = Frame(root, relief=RAISED, bd=2, bg="#8b22c3")
    frm_buttons.grid(row=0, column=0, sticky="ns")

    #create button
    open = Btn(frm_buttons, text="Open", padx=5, pady=5, cursor="hand2", relief=RAISED, command=btnObj.open_file)
    save = Btn(frm_buttons, text="Save As", row=1, padx=5, cursor="hand2", relief=RAISED, command=btnObj.save_file)
    #configure button
    open.get_grid()
    save.get_grid()


if __name__ == '__main__':
    showerror(title="Warning!", message="Run Main.py to open the editor!")