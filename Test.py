import tkinter as tk
from matplotlib.mathtext import math_to_image
from io import BytesIO
from PIL import ImageTk, Image
from kek import ScrollableImage


class Application(tk.Frame):
    def __init__(self, f, master=None):
        self.master = master
        tk.Frame.__init__(self, master)
        self.pack()
        self.fin = f
        self.createWidgets()



    def createWidgets(self):

        #Creating buffer for storing image in memory
        buffer = BytesIO()

        #Writing png image with our rendered greek alpha to buffer
        math_to_image(self.fin, buffer, dpi=250, format='png')

        #Remoting bufeer to 0, so that we can read from it
        buffer.seek(0)

        # Creating Pillow image object from it
        pimage= Image.open(buffer)

        #Creating PhotoImage object from Pillow image object
        image = ImageTk.PhotoImage(pimage)

        # #Creating label with our image
        # self.label = tk.Label(self,image=image)
        #
        # #Storing reference to our image object so it's not garbage collected,
        # # as TkInter doesn't store references by itself
        # self.label.img = image
        #
        # self.label.pack(side="bottom")
        # img = tk.PhotoImage(file=image)

        image_window = ScrollableImage(self.master, image=image, scrollbarwidth=9,
                                       width=900, height=200)
        image_window.pack()
        # self.QUIT = tk.Button(self, text="QUIT", fg="red",
        #                                     command=root.destroy)
        # self.QUIT.pack(side="top")

