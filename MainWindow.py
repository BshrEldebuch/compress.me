from tkinter import *
from tkinter import filedialog
import os
import webbrowser

from ImageSizeReducer import ImageSizeReducer

class MainWindow():

    def __init__(self, master, ImageSizeReducer):

        self.input_path = None
        self.output_path = None
        self.jpeg_quality = 10
        self.check_for_completion = None

        self.progress_label_text = StringVar()
        self.ImageSizeReducerObject = ImageSizeReducer
        self.master = master
        self.master.title("Compress.me")
        self.master.geometry("500x400")

        self.create_jpeg_field()
        self.create_input_button()

        self.create_width_height_field()

        self.create_confirmation_button()
        self.create_progress_label()
        self.label_about()
        self.button_openlink()
        self.master.mainloop()


    def create_progress_label(self):
        self.progress_label = Label(self.master, textvariable= self.progress_label_text)
        self.progress_label.pack(padx=10)

    def set_progress_label_text(self):
        if (self.check_for_completion is None):
            self.progress_label_text.set("")
        elif(self.check_for_completion == True):
            self.progress_label_text.set("Compress Completed \n Number of Converted Images: {} \n Selected folder {}"
                                        .format(self.ImageSizeReducerObject.get_num_compressed_image(), self.input_path))
        else:
            self.progress_label_text.set("Compress Failed, Check your input Folder... \n Number of Converted Images: {} \n Selected Folder {}"
                                        .format(self.ImageSizeReducerObject.get_num_compressed_image(), self.input_path))


    def run(self):
        if (self.input_path and self.jpeg_quality.get() <= 100 and self.jpeg_quality.get() > 0):
            self.ImageSizeReducerObject.set_input_path(self.input_path)
            self.ImageSizeReducerObject.set_jpg_quality(self.jpeg_quality.get())
            self.ImageSizeReducerObject.set_dim( width= self.width.get(), height=self.height.get()  )
            self.check_for_completion = self.ImageSizeReducerObject.run()
            self.set_progress_label_text()

    def create_confirmation_button(self):
        self.confirmation_button = Button(self.master, text="Start converting", command=self.run )
        self.confirmation_button.pack(padx=10)

    def create_input_button(self):
        self.input_button = Button(self.master, text = "Select Images Folder",command = self.file_dialog_input_path)
        self.input_button.pack(padx=10,pady=10)

    def create_jpeg_field(self):
        self.preview_label = Label(self.master, text="Image Quality (1 - 99) higher number produces better image quality" )
        self.jpeg_quality = IntVar(value=20)
        self.jpeg_text = Entry(self.master, textvariable = self.jpeg_quality, bd = 5)
        self.preview_label.pack()
        self.jpeg_text.pack(padx=10,pady=10)

    def create_width_height_field(self):
        self.width_height_label = Label(self.master, text="Output image size (Width then height)" )
        self.width = IntVar(value=800)
        self.height = IntVar(value=500)

        self.width_text = Entry(self.master, textvariable = self.width, bd = 5)
        self.height_text = Entry(self.master, textvariable = self.height, bd = 5)

        self.width_height_label.pack()
        self.height_text.pack(padx=10)
        self.width_text.pack()

    def file_dialog_input_path(self):
        self.input_path = filedialog.askdirectory(initialdir="//",title='Please select a directory')

    def file_dialog_output_path(self):
        self.output_path = filedialog.askdirectory(initialdir="//",title='Please select a directory')

    def label_about(self):
        self.about_label = Label(self.master, text="Made possible by Besher Eldebuch && Waleed Alrashed" )
        self.about_label.pack(padx=1,pady=1)

    def button_openlink(self):
        self.Btn = Button(self.master, text = "Linkedin Profile",command=self.openweb)
        self.Btn.pack()

    def get_input_path(self):
        return self.input_path
    
    def get_output_path(self):
        return self.output_path
    
    def get_jpeg_quality(self):
        self.jpeg_quality

    def openweb(self):
        url = "https://www.linkedin.com/in/beshr-eldebuch/"
        webbrowser.open(url,new=1)

