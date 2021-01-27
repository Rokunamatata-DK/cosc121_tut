class Gingle:
    """asd"""

    def __init__(self, name, num_legs , weight):
        """asd"""
        self.name = name
        self.num_legs = num_legs
        self.weight = weight

    def __str__(self):
        """asd"""
        return "Gingle('{}', {}, {:.2f})".format(self.name, self.num_legs, self.weight)

    def can_run(self):
        """asd"""
        
        return self.num_legs >= 2

golly = Gingle("Gargle", 23, 11.1)
print("Name:", golly.name)
print("Legs:", golly.num_legs)
print("Weight:", golly.weight)
golly = Gingle("Gargle", 23, 11.1)
print(golly.can_run())