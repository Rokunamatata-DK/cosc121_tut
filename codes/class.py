class Funger:
    """Defines the Funger  class.
    Data attributes: role  of type str
                     name  of type str
                     health  of type float    
    """

    def __init__(self, role, name, health):
        """Creates a new Funger object"""
        if role not in ['Greebling', 'Throve', 'Plaguelet']:
            raise ValueError("Invalid Funger role")
        else:
            self.role = role
        
        self.name = name

        if health < 0:
            self.health = 0
        else:
            self.health = health

    def __str__(self):
        """asd"""
        return '{0} ({1}), health = {2:.1f}'.format(self.name, self.role, self.health)

    def suffer(self, number):
        """asd"""
        self.health -= number
        if self.health < 0:
            self.health = 0

    def drink_health_potion(self, number):
        """asd"""
        self.health += number




fester = Funger('Throve', 'Walter', 10.500)

print(fester)


poxer = Funger('Plaguelet', 'Angus', 0.1)
print(poxer)
peter = Funger('Greebling', 'Pedro', 0)
print(peter)

fester = Funger('Throve', 'Walter', 10.491)
print(fester)
fester.suffer(10.4)
print(fester)
fester.suffer(2)
print(fester)
fester.drink_health_potion(0.7)
print(fester)


try:
    oof = Funger('Famine', 'Fred', 0)
    print("Did you forget to raise an exception?")
except ValueError as e:
    print(e)