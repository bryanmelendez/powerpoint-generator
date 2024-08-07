# GUI for powerpoint generator

import os
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import *


class GUI:
    def __init__(self):
        # Private vars

        self.__root = tkinter.Tk(className='Cara Mia Designs')
        # stores the string from entry box
        self.__name_entry_string = tkinter.StringVar()
        # the entry box itself
        self.__name_entry_box = None
        # window frame
        self.__frm = None
        self.__status_message = None
        self.__directory_message = None

        # Public vars

        # the name var to be accessed by user
        self.name = None
        self.file_name = None
        self.directory = None

    def create_frame(self):
        self.__frm = ttk.Frame(self.__root, padding=10)
        self.__frm.pack()

    def create_entry_boxes(self):
        ttk.Label(self.__root, text='Insert Client Name').pack()
        self.__name_entry_box = ttk.Entry(self.__root,
                                          textvariable=self.__name_entry_string).pack()

    def submit(self):
        # Getting the string from the tk variable
        self.name = self.__name_entry_string.get()

        if self.name == '' or self.directory == '':
            # convert this to gui message later
            self.set_status_message("No name entered and/or directory selected")
            return

        self.__root.destroy()

    def folder_search(self):
        self.directory = filedialog.askdirectory(mustexist=True,
                                                 initialdir=os.path.expanduser("~"))

        if self.directory == None:
            self.set_directory_message("Error: no directory selected")
            return

        #update the gui so it shows the path
        self.set_directory_message("Directory selected: {}".format(self.directory))

    def set_directory_message(self, message):
        self.__directory_message = Message(self.__root, text=message)

    def set_status_message(self, message):
        self.__status_message = Message(self.__root, text=message)
        self.__status_message.config(bg='lightgreen')

    def create_gui_window(self):
        self.__root.geometry("750x250")
        self.create_frame()

        self.create_entry_boxes()

        ttk.Label(self.__frm, text='Select the folder containing images').pack()

        # Folder search button
        ttk.Button(self.__frm, text='Folder Search', command=self.folder_search).pack()

        self.set_directory_message('No directory chosen')
        self.__directory_message.pack()

        # Submit button
        ttk.Button(self.__frm, text='Submit', command=self.submit).pack()

        self.set_status_message('Setup')
        self.__status_message.pack()

    def start_gui(self):
        self.__root.mainloop()

    def get_client_name(self):
        return self.name

    def get_file_name(self):
        return self.file_name


# driver code
gui = GUI()
gui.create_gui_window()

gui.start_gui()


'''

What do we need:

- 2 textboxes - entry
- 1 button
- title
- image of logo
- spacing and window size
- status messages - (tkinter message, green if success, red if error)
- text boxes for instructions

'''
