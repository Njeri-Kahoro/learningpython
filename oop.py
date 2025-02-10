#object oriented programming
class Person:
    def __init__(self, name, age):

        #this is a constructor method
        #it takes two parameters and initialize it as attributes

        self.name = name
        self.age = age
    def myfunction(self):
            print(f'Hello, my name is {self.name} and my age is {self.age}')

             #this is a method function
            #create an object or an instance of a class

myobj = Person('Lilly', 36)
myobj.myfunction()

myobj = Person('Emma', 26)
myobj.myfunction()

myobj = Person('Munga', 1)
myobj.myfunction()

myobj = Person('Kinyash', 12)
myobj.myfunction()

myobj = Person('Kinyua', 18)
myobj.myfunction()

myobj = Person('Njeri', 23)
myobj.myfunction()