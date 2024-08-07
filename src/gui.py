# GUI for powerpoint generator

import os
from tkinter import Tk, Message, ttk, filedialog, StringVar
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
        self.__directory_message = None
        self.__image_label = None
        self.__image_file = 'assets/logo.png'

        # Public vars

        # the name var to be accessed by user
        self.name = None
        self.file_name = None
        self.directory = None

    def create_frame(self):
        self.__frm = ttk.Frame(self.__root, padding=10)
        self.__frm.pack()

    def create_entry_boxes(self):
        ttk.Label(self.__frm, text='Insert Client Name').pack()
        self.__name_entry_box = ttk.Entry(self.__frm,
                                          textvariable=self.__name_entry_string).pack()

        ttk.Label(self.__frm, text='Save file as:').pack()
        self.__save_file_entry_box = ttk.Entry(self.__frm,
                                               textvariable=self.__save_file_string).pack()

    def submit(self):
        # Getting the string from the tk variable
        self.name = self.__name_entry_string.get()
        self.file_name = self.__save_file_string.get()

        if self.name == '' or self.directory == '' or self.file_name == '':
            # convert this to gui message later
            self.set_status_message("Error: missing an entry")
            print("Error: missing an entry")
            return

        self.__root.destroy()

    def folder_search(self):
        self.directory = filedialog.askdirectory(mustexist=True,
                                                 initialdir=os.path.expanduser("~"))

        if self.directory == None:
            self.set_directory_message("Error: no directory selected")
            print("Error: no directory selected")
            return

        #update the gui so it shows the path
        self.set_directory_message("Directory selected: {}".format(self.directory))

    def set_directory_message(self, message):
        self.__directory_message.config(text=message)

    def set_status_message(self, message):
        self.__status_message.config(text=message)

    def create_gui_window(self):
        self.__root.geometry("750x450")
        self.create_frame()

        # adding an image
        new_image = Image.open(self.__image_file)
        photo = ImageTk.PhotoImage(new_image)
        # adding image to label
        self.__image_label = ttk.Label(self.__frm, image=photo).pack()

        self.create_entry_boxes()

        ttk.Label(self.__frm, text='Select the folder containing images').pack()

        # Folder search button
        ttk.Button(self.__frm, text='Folder Search', command=self.folder_search).pack()

        self.__directory_message = ttk.Label(self.__frm, text='No directory chosen').pack()

        # Submit button
        ttk.Button(self.__frm, text='Submit', command=self.submit).pack()

        self.__status_message = ttk.Label(self.__frm, text="Press 'Submit' when ready").pack()

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


# driver code
gui = GUI()
gui.create_gui_window()

gui.start_gui()

print(gui.get_client_name())
print(gui.get_file_name())
print(gui.get_directory_path())


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
