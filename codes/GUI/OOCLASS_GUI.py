from tkinter import *
from tkinter.ttk import *

TEMPLATE = "Name: {0}\nHeight: {1:.2f} m\nHorns: {2}"

class Blork(object):
    """Defines the Blork class.
    Note that we've declared this explicitly as a subclass of object.
    Data attributes: name of type str
                     height (metres) of type float
                     has_horns of type bool    
    """

    def __init__(self, name, height, has_horns=False):
        """Blork constructor"""
        self.name = name
        self.height = height
        self.has_horns = has_horns
        

class BlorkGui(object):
    """Defines the Blork Interface
       Note that we've declared this explicitly as a subclass of object.
    """
    
    def __init__(self, window, blorks):
        """Setup the label and button on given window"""
        # self.blorks = blorks
        
        # Combo Box
        # Your combo box code goes here
        self.blorks=blorks
        blork_list = []
        for name in blorks:
            blork_list.append(name)
            
        self.names = Combobox(window,
                                values=blork_list,
                                font=("Arial", 10))
        self.names.set(blork_list[0])
        self.names.grid(row=0, column=0)
        # View Button
        # Your button code goes here
        self.btn= Button(window,text="View details",command=self.display)
        self.btn.grid(row=0, column=1)
        # Details Label
        # Your label code goes here 
        self.display= Label(window,text="Press 'View details'")
        self.display.grid(row=1, column=0,padx=(10,0))
    # Your button function goes here

    def display(self):
        result= self.blorks[self.names.get()]
        has_h=""
        if result.has_horns==True:
            has_h="Yes"
        else:
            has_h="No"

        self.display['text']="Name: "+result.name+"\nHeight: "+"{0:.2f}".format(result.height)+" m\nHorns: "+has_h

def main():
    """Set up the GUI and run it."""    
    blork_dict = {"Jeff": Blork("Jeff", 1.6),
              "Lily": Blork("Lily", 1.111111),
              "Jack": Blork("Jack", 1.89),
              "Chewblorka": Blork("Chewblorka", 3.14, True),
              "Blorkstien": Blork("Blorkstien", 0.856, True)}
    # for a in blork_dict:
    #     print(a,blork_dict[a])
    window = Tk()
    blork_gui = BlorkGui(window, blork_dict)
    window.mainloop()

main()