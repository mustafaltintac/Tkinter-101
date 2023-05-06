import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("geometry manager")

#pack

# red=tk.Button(window,text="red",fg="red",)
# red.pack(side=tk.LEFT)
# green=tk.Button(window,text="green",fg="green",)
# green.pack(side=tk.LEFT)
# blue=tk.Button(window,text="blue",fg="blue",)
# blue.pack(side=tk.LEFT)


# orange=tk.Button(window,text="orange",fg="orange")
# orange.pack(side=tk.BOTTOM)
# brown=tk.Button(window,text="brown",fg="brown")
# brown.pack(side=tk.BOTTOM)


# gray=tk.Button(window,text="gray",fg="gray")
# gray.pack(side=tk.TOP,fill=tk.BOTH,expand=TR)

# GRİD

# for r in range(5):
#     for c in range(5):
#         label=tk.Label(window,text= 'R%s/C%s'%(r,c),borderwidth=3)
#         label.grid(row=r,column=c,padx=3,pady=3)

#PLACE

label=tk.Label(window,text="place")
label.place(x=15,y=15)      #pixel olarak ayarlar


label=tk.Label(window,text="place")
label.place(relx=(0.3),rely=(0.3))  # oransal olarak ayarlar





















window.mainloop()