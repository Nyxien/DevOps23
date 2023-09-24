'''
class Person:
    def __init__(self):
        self.name = input("Vad heter personen? ")
        self.age = input("Hur gammal är personen? ")
        self.address = input("Vad bor personen? ")

    def person_description(self):
        print(f"Personen heter {self.name}, är {self.age} år gammal och bor i {self.address}.")

# Create an instance of the Person class
person = Person()

# Call the person_description method to display the person's information
person.person_description()
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14 * self.radius

radius = float(input("Ange radien på cirkeln: "))

circle = Circle(radius)

print(f"Omkretsen på cirkeln är {circle.circumference()}")
