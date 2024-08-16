# GUI for powerpoint generator

import os
import sys
from tkinter import Tk, ttk, filedialog, StringVar, Message
from PIL import Image, ImageTk


class GUI:
    def __init__(self):
        # Private vars

        self.__root = Tk(className='Cara Mia Designs')
        # stores the string from entry box
        self.__name_entry_string = StringVar()
        # the entry box itself
        self.__name_entry_box = None
        # save file name string
        self.__save_file_string = StringVar()
        # save file name entry box
        self.__save_file_entry_box = None
        # window frame
        self.__frm = None
        self.__status_message = None
        self.__folder_label = None
        self.__directory_message = None
        self.__image_label = None
        self.__image_file = self.get_image_asset()
        # storing the photo in an instance
        self.__photo = None
        self.__folder_button = None
        self.__submit_button = None
        self.__save_file_label = None
        self.__name_label = None

        # Public vars

        # the name var to be accessed by user
        self.name = None
        self.file_name = None
        self.directory = None

        # make the window
        self.create_gui_window()

    def get_image_asset(self):
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            print('running in a PyInstaller bundle')
            image_file = os.path.join(sys._MEIPASS, 'assets/logo.png')
        else:
            print('running in a normal Python process')
            image_file = os.path.abspath('assets/logo.png')

        print(image_file)
        return image_file


    def create_frame(self):
        self.__frm = ttk.Frame(self.__root, padding=10)
        self.__frm.pack()

    def submit(self):
        # Getting the string from the tk variable
        self.name = self.__name_entry_string.get()
        self.file_name = self.__save_file_string.get()

        if self.name == '' or self.directory is None or self.file_name == '':
            # convert this to gui message later
            self.set_status_message("Error: missing an entry", 'red')
            print("Error: missing an entry")
            return

        self.__root.destroy()

    def folder_search(self):
        self.directory = filedialog.askdirectory(mustexist=True,
                                                 initialdir=os.path.expanduser("~"))

        print("Directory: {}".format(self.directory))
        if not os.path.exists("{}".format(self.directory)):
            self.set_directory_message("Error: no directory selected", 'red')
            print("Error: no directory selected")
            return

        # update the gui so it shows the path
        self.set_directory_message("Directory selected: {}".format(self.directory), 'lightgreen')

    def set_directory_message(self, message, color):
        self.__directory_message.config(text=message, bg=color)

    def set_status_message(self, message, color):
        self.__status_message.config(text=message, bg=color)

    def create_gui_window(self):
        self.__root.geometry("750x450")
        self.create_frame()

        # adding an image
        new_image = Image.open(self.__image_file)
        self.__photo = ImageTk.PhotoImage(new_image)
        # adding image to label
        self.__image_label = ttk.Label(self.__frm, image=self.__photo)

        self.__name_label = ttk.Label(self.__frm, text='Client name:')
        self.__name_entry_box = ttk.Entry(self.__frm,
                                          textvariable=self.__name_entry_string)

        self.__save_file_label = ttk.Label(self.__frm, text='Save file as:')
        self.__save_file_entry_box = ttk.Entry(self.__frm,
                                               textvariable=self.__save_file_string)

        self.__folder_label = ttk.Label(self.__frm,
                                        text='Select the folder containing images')

        # Folder search button
        self.__folder_button = ttk.Button(self.__frm,
                                          text='Folder Search',
                                          command=self.folder_search)

        self.__directory_message = Message(self.__frm,
                                           text='No directory chosen',
                                           width=10000, aspect=5000)

        # Submit button
        self.__submit_button = ttk.Button(self.__frm,
                                          text='Submit',
                                          command=self.submit)

        self.__status_message = Message(self.__frm,
                                        text="Press 'Submit' when ready",
                                        width=10000, aspect=5000)

        # pack everything
        self.__image_label.pack(pady=5)
        self.__name_label.pack()
        self.__name_entry_box.pack(pady=5)
        self.__save_file_label.pack()
        self.__save_file_entry_box.pack(pady=5)
        self.__folder_label.pack()
        self.__folder_button.pack(pady=5)
        self.__directory_message.pack(pady=5)
        self.__submit_button.pack(pady=5)
        self.__status_message.pack(pady=5)

    # TODO Make this better
    def start_gui(self):
        self.__root.mainloop()

    # Getter functions:

    def get_client_name(self):
        return self.name

    def get_file_name(self):
        return self.file_name

    def get_directory_path(self):
        return self.directory
