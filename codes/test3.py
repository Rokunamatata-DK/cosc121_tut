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
        self.baranges = 0
    
    def say_hello(self):
        """asd"""
        if self.has_horns:
            print("Hi! My name is {name}!".format(name=self.name).upper())
        else:
            print("Hi! My name is {name}!".format(name=self.name))
       
        
    def __str__(self):
        """asd"""
        if  self.has_horns == False:
            return"{name} is a {height:.2f} m tall blork!".format(\
            name=self.name, height=self.height)
        elif self.has_horns == True:
            return"{name} is a {height:.2f} m tall horned blork!".format(\
            name=self.name, height=self.height)
            
    def collect_baranges(self, number=None):
        """asd"""
        if number == None:
            self.baranges += 1
        else:
            self.baranges += number
        
        
   
            
    def eat(self):
        """asd"""
        if self.baranges == 0:
            print("I don't have any baranges to eat!")
        else:
            self.baranges -= 1
            self.height += 0.1
        
    def feast(self):
        """asd"""
        if self.baranges >= 5:
            
            self.baranges -= 5
            if self.has_horns == True:
                self.height *= 1.5
            else:
                self.has_horns = True
            
        else:
            print("I don't have enough baranges to feast!")
        
        
        
        
hungry_blork = Blork("Jack", 1.89)
hungry_blork.collect_baranges()
hungry_blork.eat()
print(hungry_blork)       
        
hungry_blork = Blork("Jeff", 1.6)
print(hungry_blork)
hungry_blork.collect_baranges()
hungry_blork.eat()
print(hungry_blork)

mighty_blork = Blork("Chewblorka", 3.14, True)
print("Baranges: {}".format(mighty_blork.baranges))
mighty_blork.collect_baranges(9)
print("Baranges: {}".format(mighty_blork.baranges))
mighty_blork.feast()
print("Baranges: {}".format(mighty_blork.baranges))
print(mighty_blork)

nice_blork = Blork("Lily", 1.11111111111111)
nice_blork.eat()