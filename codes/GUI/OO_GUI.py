"""Demonstrate event binding and variable tracing, 
   this time with a clean OO design.
"""

from tkinter import *
from tkinter.ttk import *

class GreetingGui:
    """The GUI class"""

    def __init__(self, window):
        """Setup the label and button on given window"""

        self.click_count=0

        self.hello_label = Label(window, text='0')
        self.hello_label.grid(row=0, column=0)

        self.hello_button = Button(window, text="+1", command=self.say_hello)
        self.hello_button.grid(row=1, column=0)

        self.btn_2 = Button(window, text="-1", command=self.minus_1)
        self.btn_2.grid(row=1, column=1)

   
    def say_hello(self):
        """The event handler for clicks on the button"""
      
        self.click_count += 1

        self.hello_label['text'] =   self.click_count.__str__()

    def minus_1(self):
        """The event handler for clicks on the button"""
        
        self.click_count -= 1

        self.hello_label['text'] =self.click_count.__str__()

def main():
    """Set up the GUI and run it."""
    window = Tk()
    greeting_gui = GreetingGui(window)
    window.mainloop()

main()