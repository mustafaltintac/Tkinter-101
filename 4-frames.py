import tkinter as tk
from tkinter import ttk


window=tk.Tk() #high level frame

# FRAME

# leftFrame=tk.Frame(window,width=540,height=640,bg="red")
# leftFrame.grid(row=0,column=0 ,padx=10,pady=10)

# rightFrame=tk.Frame(window,width=540,height=640,bg="yellow")
# rightFrame.grid(row=0,column=1 ,padx=10,pady=10)

# leftFrame1=tk.LabelFrame(leftFrame,text="frame 1",width=540,height=320,bg="blue")
# leftFrame1.grid(row=0,column=0 ,padx=10,pady=10)

# leftFrame2=tk.LabelFrame(leftFrame,text="frame 2",width=540,height=320,bg="orange")
# leftFrame2.grid(row=1,column=0 ,padx=10,pady=10)

# label=tk.Label(leftFrame2,text="label ",bg="white",activebackground="white")
# label.grid(row=0,column=0,padx=2)


#PANED WINDOW

pw=ttk.PanedWindow(window,orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH,expand=True)

m2=ttk.PanedWindow(pw,orient=tk.VERTICAL)

frame2=ttk.Frame(pw,width=720,height=400,relief=tk.RIDGE)
frame3=ttk.Frame(pw,width=720,height=240,relief=tk.RIDGE)

m2.add(frame2)
m2.add(frame3)

frame1=ttk.Frame(pw,width=360,height="640",relief=tk.GROOVE)
pw.add(m2)
pw.add(frame1)





window.mainloop()


