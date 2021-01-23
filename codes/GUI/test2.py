from tkinter import *
from tkinter.ttk import *

# Write your functions here
def change_lable():
    global value, value_label
    value_label['text']=value.__str__()

def subtract_five():
    global value, value_label
    value-=5
    change_lable()

def subtract_one():
    global value, value_label
    value-=1
    change_lable()
def add_one():
    global value, value_label
    value+=1
    change_lable()
def add_five():
    global value, value_label
    value+=5
    change_lable()



def main():
    """Set up the GUI and run it"""

    global value, value_label
    window = Tk()
    value = 0
    value_label = Label(window, text=str(value))
    value_label.grid(row=0, column=0, columnspan=4)
    subtract_five_button = Button(window, text="-5", command=subtract_five)
    subtract_five_button.grid(row=1, column=0)
    subtract_one_button = Button(window, text="-1", command=subtract_one)
    subtract_one_button.grid(row=1, column=1)
    add_one_button = Button(window, text="+1", command=add_one)
    add_one_button.grid(row=1, column=2)
    add_five_button = Button(window, text="+5", command=add_five)
    add_five_button.grid(row=1, column=3)
    window.mainloop()

main()