from tkinter import Tk, ttk
from tkinter.font import Font


class StatusGui:
    def __init__(self, message):
        # Create root window
        self.__root = Tk(className='Cara Mia Designs')
        self.__root.geometry("750x450")

        # Create frame
        self.__frm = ttk.Frame(self.__root, padding=10)
        self.__frm.pack()

        # Set labels for status info
        self.__status_label = ttk.Label(self.__frm,
                                        text=message,
                                        font=Font(self.__root, 25))
        self.__status_label.pack(pady=10)

        self.__prompt_label = ttk.Label(self.__frm,
                                        text='You may close this window',
                                        font=Font(self.__root, 25))
        self.__prompt_label.pack()

        self.__root.mainloop()
