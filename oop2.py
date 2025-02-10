#using oop create a class called cars that have the following attributes model, colour and year of manufacture.
# Implement constructor method and a method function that prints 'My favourite car is ....., its ..... in coulour and
# manufacture in ..... year.


#create five instance of that class

class Car:
    def __init__(self, make, colour, year):

        self.make = make
        self.colour = colour
        self.year = year
    def myfunction(self):
        print(f'My favourite car is {self.make}, it is {self.colour} in colour and its year of manufacture is {self.year}')

myobj = Car('Ford Raptor', 'black', 2000)
myobj.myfunction()

myobj = Car('Mazda CX5', 'ruby red', 2014)
myobj.myfunction()

myobj = Car('Toyota Axio', 'white', 2008)
myobj.myfunction()

myobj = Car('Mazda Axela', 'blue', 2015)
myobj.myfunction()

myobj = Car('Toyota Harrier', 'matte black', 2002)
myobj.myfunction()