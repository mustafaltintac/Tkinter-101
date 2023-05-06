import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

Window=tk.Tk()
Window.geometry("500x400")
Window.title("digital asistance")


def buttonFunction():
    print("push button")

    #label yazı değiştirme
    label.config(text="merhaba dünya",font="Times 20", bg="red",fg="yellow")

    #entry
    value=entry.get()
    label.configure(text=value)
    entry.configure(state="disabled")

    #messagebox
    message_box=messagebox.showinfo(title="info",message="information")
    message_box=messagebox.askokcancel(title="info",message="information")
    message_box=messagebox.askretrycancel(title="info",message="information")
    message_box=messagebox.askquestion(title="info",message="information",)
    print(message_box)

#button
button=tk.Button(Window,text="button",activebackground="green",bg="yellow",fg="purple",activeforeground="orange",height=10,width=200,
                 command=buttonFunction)
button.pack()
#label
label=tk.Label(Window,text="hello world",font="Times 16", fg="black",bg="white",wraplength=50)
label.pack(side=tk.RIGHT,padx=10)

#entry
entry=tk.Entry(Window,width=50)
entry.pack(side=tk.LEFT,padx=10)

Window.mainloop()
