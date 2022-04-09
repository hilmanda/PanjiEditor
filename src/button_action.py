from tkinter import *
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfile, asksaveasfile
from types import NoneType

#class for button
class Button_action():
    def __init__(self, root, txt_edit):
        self.__filename = None
        self.__root = root
        self.__text = txt_edit

    def new_file(self, *args):
        self.__filename = None
        self.__text.delete(1.0,END)

    #open a file method
    def open_file(self, *args):
        try:
            file = askopenfile(mode='r')
            self.__filename = file.name
            text = file.read()
            self.__text.delete(1.0, END)
            self.__text.insert(1.0, text)

            self.__root.title(f'PanjiEditor - {self.__filename}')
        except AttributeError:
            print('No file Chosen')
    
    #save to file method
    def save_file(self, *args):
        try:
            text = self.__text.get(1.0, END)
            file = open(self.__filename, 'w')
            file.write(text)
            file.close()
        except: #if its a new file
            print("Create New File")
            self.saveas_file()

    #saveAs file method
    def saveas_file(self):
        try:
            file = asksaveasfile(defaultextension="txt", filetypes=[("Text Files", ".txt"), ("All Files", ".*")],)
            self.__filename = file.name
            text = self.__text.get(1.0, END)
            file.write(text)
            self.__root.title(f"PanjiEditor - {self.__filename}")

        except AttributeError:
            print("No file Chosen")


#create button
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
    frame_buttons = Frame(root, relief=RAISED, bd=2, bg="#8b22c3")
    frame_buttons.grid(row=0, column=0, sticky="ns")

    #create button
    new = Btn(frame_buttons, text="New File", padx=5, pady=5, cursor="hand2", relief=RAISED, command=btnObj.new_file)
    open = Btn(frame_buttons, text="Open", row=1, padx=5, cursor="hand2", relief=RAISED, command=btnObj.open_file)
    save = Btn(frame_buttons, text ="Save", row=2, padx=5, pady=5, cursor="hand2", relief=RAISED, command=btnObj.save_file)
    saveAs = Btn(frame_buttons, text="Save As", row=3, padx=5, cursor="hand2", relief=RAISED, command=btnObj.saveas_file)
    
    #configure button
    new.get_grid()
    open.get_grid()
    save.get_grid()
    saveAs.get_grid()

    #shortcut
    txt_editor.bind('<Control-n>', btnObj.new_file)
    txt_editor.bind('<Control-s>', btnObj.save_file)
    txt_editor.bind('<Control-o>', btnObj.open_file)


if __name__ == '__main__':
    showerror(title="Warning!", message="Run Main.py or Main.exe or PanjiEditor Shortcut to open the editor!")