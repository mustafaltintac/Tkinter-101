import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk , Image

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

window=tk.Tk()
window.geometry("600x400")

#filedialog

def openfile():
    file_name=filedialog.askopenfilename(initialdir = "C:/Users/MUSTAFA" , title = "select a file ...")
    print(file_name)
    img=Image.open(file_name)
    img=ImageTk.PhotoImage(img)

    label=tk.Label(window,image=img)
    label.image=img
    label.pack(padx=15,pady=15)

button=tk.Button(window,text="open file",command=openfile)
button.pack()


# plot
fig=Figure(figsize=(5,4),dpi=50)
data=np.arange(0.3,0.1)
fig.add_subplot(111).plot(data,data*2+3)

canvas=FigureCanvasTkAgg(fig,master=window)
canvas.draw()
canvas.get_tk_widget().pack()

#mouse event

def leftClick(event):
    tk.Label(window,text="left click...").pack()
    
def middleClick(event):
    tk.Label(window,text="middle click...").pack()
def rightClick(event):
    tk.Label(window,text="right click...").pack()


window.bind("<Button-1>",leftClick)
window.bind("<Button-2>",middleClick)
window.bind("<Button-3>",rightClick)
















window.mainloop()