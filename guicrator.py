from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Gui Creator")
root.geometry("900x600")

class CreateElements():
    def __init__(self):
        print("This is create element class")
    def createLabel(self):
        print("leabel in class")
        label1 = Label(root,text="This label has been created using classes",fg="red")
        label1.pack()
        print("label")
    def clickButton(self):
        messagebox.showinfo("info","You have clicked a button that had been created using classes")
    def createButton(self):
        button1 = Button(root,text="Button",command=self.clickButton)
        button1.pack()
    def createDropdown(self):
        num = [1,2,3,4]
        dropdown1 = ttk.Combobox(root,values=num)
        dropdown1.pack()        


gui_list = ["Label","Button","Dropdown"]
value_combo= StringVar()
dropdown = ttk.Combobox(root,values=gui_list,textvariable=value_combo,state="readonly")
dropdown.pack()

obj = CreateElements()

def choose():
    elements = value_combo.get()
    if elements=="Label":
        obj.createLabel()
    if elements=="Button":
        obj.createButton()
    if elements=="Dropdown":
        obj.createDropdown()

button1 = Button(root,text="Create Element",command=choose)
button1.pack(padx=20,pady=20)

root.mainloop()