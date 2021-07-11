from tkinter import *

import tkinter as tk
import tkinter.messagebox

import time
from Repository.Repository import Repository


class Window(Frame):
    repository = None
    message_number = 0

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Connect", command=self.button_click_connect)
        # self.file_menu.add_command(label="Create", command=self.button_click_create)
        self.file_menu.add_command(label="Retrieve", command=self.button_click_retrieve)
        self.file_menu.entryconfig("Retrieve", state="disabled")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_program)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = Menu(self.menu, tearoff=0)
        self.edit_menu.add_command(label="Undo")
        self.edit_menu.add_command(label="Redo")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Test", command=self.button_click_message)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        exit_button = Button(self, text="Exit", command=self.exit_program)

        # place button at (0,0)
        exit_button.place(x=0, y=0)
        
        test_button = Button(self, text="Test", command=self.button_click_message)
        test_button.place(x=50, y=0)

        self.label = Label(text="", fg="Red", font=("Helvetica", 18))
        self.label.place(x=40, y=40)
        self.update_clock()

        var2 = tk.StringVar()
        #         var2.set((1,2,3,4))
        self.lb = tk.Listbox(self, listvariable=var2)
        self.lb.place(x=50, y=70)

        self.repository = Repository()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)

    def button_click_message(self):
        self.message_number += 1
        if self.message_number == 1:
            tkinter.messagebox.showinfo('title', 'Info message text is here')

        if self.message_number == 2:
            tkinter.messagebox.showwarning('title', 'Warning message text is here')

        if self.message_number == 3:
            tkinter.messagebox.showerror('title', 'Error message text is here')
            self.message_number = 0

    def button_click_connect(self):
        self.repository.initialize_repository()
        self.file_menu.entryconfig("Retrieve", state="normal")

    def button_click_create(self):
        pass

    def button_click_retrieve(self):
        list_items = self.repository.get_language_data(year=1960)
        for item in list_items:
            self.lb.insert('end', item)

    def exit_program(self):
        self.repository.disconnect()
        exit()


root = Tk()
root.configure(background='#FAEBD7')

app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")
root.after(1000, app.update_clock)
root.mainloop()
