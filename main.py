from tkinter import Tk

from MainWindow import MainWindow
from ImageSizeReducer import ImageSizeReducer

if __name__ == "__main__":
    obj = ImageSizeReducer()
    master = Tk()
    MainWindow(master, obj)
    master.mainloop()
