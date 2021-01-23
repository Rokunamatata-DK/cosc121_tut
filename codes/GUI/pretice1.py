from tkinter import *
from tkinter.ttk import *

def main():
    abc = Tk()
    # label = Label (abc, text='this is our label')
    # label = Label(abc)
    # label['text']='this is our label'
    # # label.configure(text='this is our label')
    # label.grid(row=0, column=0)
    
    button0 = Button(abc, text="Button0")
    button1 = Button(abc, text="Button1")
    button2 = Button(abc, text="Button2")
    button3 = Button(abc, text="Button3")
    button4 = Button(abc, text="Button4")
    button5 = Button(abc, text="Button5")
    button0.grid(row=0, column=0,padx=10, pady=20)
    button1.grid(row=0, column=1, columnspan=2,sticky=(E, W),padx=10, pady=20,ipady=20)
    button2.grid(row=1, column=0, rowspan=2,sticky=(N, S),padx=10, pady=20)
    button3.grid(row=1, column=2,padx=10, pady=20)
    button4.grid(row=2, column=1,padx=10, pady=20)
    button5.grid(row=2, column=2,padx=10, pady=20)
    abc.mainloop()
main()
