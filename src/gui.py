# GUI for powerpoint generator

import os
import tkinter
from tkinter import ttk
from tkinter import filedialog


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

        # Public vars

        # the name var to be accessed by user
        self.name = None
        self.file_name = None
        self.directory = None

    def create_frame(self):
        self.__frm = ttk.Frame(self.__root, padding=10)
        self.__frm.grid()

    def create_entry_boxes(self):
        ttk.Label(self.__root, text='Insert Client Name').grid(row=1, column=0)
        self.__name_entry_box = ttk.Entry(self.__root,
                                          textvariable=self.__name_entry_string).grid(row=1, column=1)

    def submit(self):
        # Getting the string from the tk variable
        self.name = self.__name_entry_string.get()

        if self.name == '' or self.directory == '':
            # convert this to gui message later
            print("No name entered and/or directory selected")
            return

        self.__root.destroy()

    def folder_search(self):
        self.directory = filedialog.askdirectory(mustexist=True,
                                                 initialdir=os.path.expanduser("~"))

        if self.directory == None:
            print("Error: no file selected")
            return

        #update the gui so it shows the path
        print("Directory selected: {}".format(self.directory))

    def create_gui_window(self):
        self.__root.geometry("750x250")
        self.create_frame()

        self.create_entry_boxes()

        ttk.Label(self.__frm, text='Select the folder containing images').grid(row=0, column=0)

        # Folder search button
        ttk.Button(self.__frm, text="Folder Search", command=self.folder_search).grid(row=0, column=1)

        # Submit button
        ttk.Button(self.__frm, text="Submit", command=self.submit).grid(row=2, column=3)

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

print(gui.get_client_name())


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
