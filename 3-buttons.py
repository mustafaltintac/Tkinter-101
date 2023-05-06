import tkinter as tk
from tkinter import ttk


window=tk.Tk()
window.geometry("300x400")

def buttonFunciton():
    print("here")
    m=method.get()
    if(m=="1"):
        print("method1: ")
    elif(m=="2"):
        print("method2: ")
    else:
        print("method1 & method2: ")

    print(problem.get())

    values=save_var.get()
    if values==1:
        print("Saved ")
    else:
        print("not save")


button=tk.Button(window,text="button",activebackground="black",activeforeground="white",fg="yellow",bg="orange",
                 height=15,width=50,command=buttonFunciton)
button.grid(row=0 ,column=0, pady=15)


method=tk.StringVar()
radioButton=tk.Radiobutton(window,text="method1",value="1",activebackground="blue",activeforeground="orange",fg="black",bg="white",
                           height=5,width=15,borderwidth=10,variable=method)
radioButton.grid(row=1,column=0)

radioButton2=tk.Radiobutton(window,text="method2",value="2",activebackground="green",activeforeground="blue",fg="white",bg="black",
                            height=5,width=15,border=10,variable=method).grid(row=1,column=1,pady=15)

problem=tk.StringVar()
comboBox=ttk.Combobox(window,textvariable=problem,values=("1","2","3"),state="steadonly")
comboBox.grid(row=2,column=0 ,pady=15)

def checkButtomFunction():
    print("save")

save_var=tk.IntVar()
save_var.set(0)
c_button=tk.Checkbutton(window,text="save",variable=save_var,font="Times 25", activebackground="yellow",activeforeground="red",bg="blue"
                        ,command=checkButtomFunction)
c_button.grid(row=2,column=2,pady=15)














window.mainloop()