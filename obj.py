#!/usr/bin/python

class Animal(object):
    pass
   
#dog is an instance of Animal class
   
class Dog(Animal):
    def __init__(self, name):
        self.name = name
        
#cat is an instance of Animal class
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        
class Person(object):
    def __init__(self, name)
        self.name = name
        
        self.pet = None

#has-a        
class Employee(Person):
    def__init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary
        
class Fish(object):
    pass
    
class Salmon(Fish):
    pass
    
class Halibut(Fish):
    pass
    
rover = Dog("Rover") #rover is an object of animal dog, dog is a sub-class of animal class

pep = Cat("Pep")

mary.pet = Pep

frank = Employee("Frank", 2000)

crouse= Salmon()
        
        
        
        
        
        
    
