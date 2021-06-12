from tkinter import *

import tkinter as tk
import tkinter.messagebox

import time
from database import Database


class Window(Frame):
    data = None
    message_number = 0

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master
        
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu, tearoff=0)
        fileMenu.add_command(label="Connect", command=self.buttonClickConnect)
        fileMenu.add_command(label="Create", command=self.buttonClickCreate)
        fileMenu.add_command(label="Retrieve", command=self.buttonClickRetrieve)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu, tearoff=0)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        editMenu.add_separator()
        editMenu.add_command(label="Test", command=self.buttonClickMessage)
        menu.add_cascade(label="Edit", menu=editMenu)
        
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.exitProgram)

        # place button at (0,0)
        exitButton.place(x=0, y=0)
        
        self.label = Label(text="", fg="Red", font=("Helvetica", 18))
        self.label.place(x=40,y=40)
        self.update_clock()
        
        var2 = tk.StringVar()
#         var2.set((1,2,3,4))
        self.lb = tk.Listbox(self, listvariable=var2)
        self.lb.place(x=50, y=70)
        
        self.data = Database()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)

    def buttonClickMessage(self):
        self.message_number += 1
        if self.message_number == 1:
            tkinter.messagebox.showinfo('title', 'Info message')
            
        if self.message_number == 2:
            tkinter.messagebox.showwarning('title', 'Warning message')
        
        if self.message_number == 3:
            tkinter.messagebox.showerror('title', 'Error message')
            self.message_number = 0
        
    def buttonClickConnect(self):
        self.data.connect()

    def buttonClickCreate(self):
        self.data.create_table()

    def buttonClickRetrieve(self):
        list_items = self.data.fetch_data(year=1930)
        for item in list_items:
            self.lb.insert('end', item)


    def exitProgram(self):
        self.data.disconnect()
        exit()
 
        
root = Tk()
root.configure(background='#FAEBD7')

app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")
root.after(1000, app.update_clock)
root.mainloop()