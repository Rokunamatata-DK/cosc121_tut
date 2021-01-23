from tkinter import *
from tkinter.ttk import *

##GUI test
def cal():
    global name_entry,name_entry2,fruit_combobox,display
    op = fruit_combobox.get()
    n1= int( name_entry.get())
    n2= int( name_entry2.get())
    result=0
    if op =="+":
        result=n1+n2
    elif op == "-":
         
        result=n1-n2
    else:
        result=n1*n2
    display['text']=result.__str__()

def main():
    window = Tk()
    global name_entry,name_entry2,fruit_combobox,display
    name_entry = Entry(window)
    name_entry.grid(row=0, column=0)


    fruit_choices = ["+", "-", "*"]
    fruit_combobox = Combobox(window,
                              values=fruit_choices,
                              font=("Arial", 10))
    fruit_combobox.set("+")
    fruit_combobox.grid(row=0, column=1, padx=20, pady=40)

    name_entry2 = Entry(window)
    name_entry2.grid(row=0, column=2)

    display = Label( window ,text="= ")
    display.grid(row=0, column=3)
    
    btn = Button(window, text="Calculate", command=cal)
    btn.grid(row=1, column=0, columnspan=3)

    window.mainloop()

    



main()