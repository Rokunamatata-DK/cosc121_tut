"""File for creating Person objects"""

class Person:
    """Defines a Person class, suitable for use in a hospital context.
    Data attributes: name of type str
                     age of type int
                     weight (kg) of type float
                     height (metres) of type float
    Methods: bmi()
    """

    def __init__(self, name, age, weight, height):
        """Creates a new Person object with the specified name, age, weight
           and height"""
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def bmi(self):
        """Returns the body mass index of the person"""
        return self.weight / (self.height * self.height)
        
    # *** YOUR CODE *** Define a status method here.
    def status(self):
        """asd"""
        bmi_number = self.bmi()
        if bmi_number < 18.5:
            return "Underweight"
        elif bmi_number >= 18.5 and bmi_number < 25:
            return "Normal"
        elif bmi_number >= 25 and bmi_number < 30:
            return "Overweight"
        else:
            return "Obese"
    def __str__(self):
        """Returns the formatted string representation of the Person object"""
        template = "{0} ({1}) has a bmi of {2:3.2f}. Their status is {3}."
        return template.format(self.name, self.age, self.bmi(), self.status())
    
def read_people(csv_filename):
    """asd"""
    infile = open(csv_filename)
    
    persons = []
    
    for line in infile:
        data = line.split(',')
        persons.append(Person(data[0], int(data[1]), \
            float(data[2]), float(data[3])))
        
    return persons

def filter_people(people, status_string):
    """asd"""
    result = []
    for person in people:
        if person.status() == status_string:
            result.append(person)

    return result

def age_value(person):
    """asd"""
    return person.age

def bmi_value(person):
    """asd"""
    return person.bmi()






bods = read_people("Z:\Tutor 2021\cosc212\code\people1.csv")
bods.sort(key=age_value)
for bod in bods:
    print(bod)


bods = read_people("Z:\Tutor 2021\cosc212\code\people1.csv")
bods.sort(key=bmi_value)
for bod in bods:
    print(bod)