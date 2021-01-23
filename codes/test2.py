class Blork:
    """Defines the Blork class.
    Data attributes: name of type str
                     height (metres) of type float
                     has_horns of type bool    
    """

    def __init__(self, name, height, has_horns=False):
        """Creates a new Blork object"""
        self.name = name
        self.height = height
        self.has_horns = has_horns
    
    def say_hello(self):
        """asd"""
        if self.has_horns:
            result_name=self.name.upper()
        else:
            result_name=self.name
        print("Hi! My name is {name}!".format(name=result_name))

mighty_blork = Blork("Chewblorka", 3.14, True)
mighty_blork.say_hello()
first_blork = Blork("Jeff", 1.6)
first_blork.say_hello()
