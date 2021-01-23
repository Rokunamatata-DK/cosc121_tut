from tkinter import *
from tkinter.ttk import *

# Insert some code here (hint: event handlers)
def say_hello():
    global message_label

    message_label['text'] = "Kia ora!"

def say_goodbye():
    global message_label

    message_label['text'] = "Noho ora mai"


def main():
    """Construct the GUI and run it"""

    global message_label
    window = Tk()
    message_label = Label(window, text="Click a button!")
    message_label.grid(row=0, column=0)

    # Insert some code here (hint: buttons)
    btn_hello = Button(window, text="Say hello",command=say_hello)
    btn_hello.grid(row=1, column=0)
    
    btn_goodbye = Button(window, text="Say goodbye",command=say_goodbye)
    btn_goodbye.grid(row=1, column=1)

    window.mainloop()

main()