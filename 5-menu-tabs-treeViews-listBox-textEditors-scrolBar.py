import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.geometry("600x400")

# MENU

menuBar=tk.Menu(window)
window.config(menu=menuBar)

file=tk.Menu(menuBar)
edit=tk.Menu(menuBar)

menuBar.add_cascade(label="file" , menu=file)
menuBar.add_cascade(label="edit" , menu=edit)

def fileFunction():
    print("new file")

def editFunction():
    print("undo")
file.add_command(label="new file", command=fileFunction)
edit.add_command(label="undo", command=editFunction)

#TABS

tabs=ttk.Notebook(window,width=500,height=300)
tabs.place(x=25,y=25)

tab1=ttk.Frame(tabs,width=50,height=50)
tab2=ttk.Frame(tabs,width=50,height=50)
tab3=ttk.Frame(tabs,width=50,height=50)

tk.Label(tab1,text="label 1").pack()
tk.Label(tab2,text="labe 2").pack()
# tk.Label(tab3,text="label 3").pack()

tabs.add(tab1,text="tree view")
tabs.add(tab2,text="list box")
tabs.add(tab3,text="text editor")

#TREE VİEWS

treeView=ttk.Treeview(tab1)
treeView.place(x=5,y=5)

treeView.insert("","0","item1",text="spain")
treeView.insert("item1","1","item2",text="madrid")
treeView.insert("","2","item3",text="france")
treeView.insert("item3","3","item4",text="paris")

def callback(event):
    item=treeView.identify("item",event.x,event.y)
    print(item)


treeView.bind("<Double-1>",callback)

# LİST BOX

listBox=tk.Listbox(tab2, selectmode=tk.MULTIPLE)
listBox.insert(0,"spain")
listBox.insert(1,"france")
listBox.insert(2,"portugal")
listBox.place(x=5,y=5)
def getItem():
    index_list=listBox.curselection()
    print(index_list)
    for each in index_list:
        print(listBox.get(each))

button=tk.Button(tab2,text="button",command=getItem)
button.place(x=150, y=15)

#Text editor

textEditor=tk.Text(tab3,width=25,height=25,wrap=tk.WORD)
textEditor.grid(row=0,column=0,padx=10,pady=10)

def textEditorFunction():
    print(textEditor.get(1.0,tk.END))

button=tk.Button(tab3,text="save",command=textEditorFunction)
button.grid(row=0,column=2,padx=10,pady=10)

# scroll

scroll=tk.Scrollbar(tab3,orient=tk.VERTICAL,command=textEditor.yview)
scroll.grid(row=0,column=1,sticky= tk.N + tk.S)
textEditor.config(yscrollcomman=scroll.set)





































window.mainloop()