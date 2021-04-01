# Class Coding
# Chapter 26 only had an intro to OOP

class Employee:
    def setName(self, value):
        self.name = value
    
    def displayName(self):
        print(self.name)

emp1 = Employee()
emp2 = Employee()
emp1.setName('Karun')
emp2.setName('Vijay')

emp2.displayName()
emp1.displayName()

# can add new fields to a class instance
emp1.newField = 3.14
emp1.newField # shows 3.14

class Developer(Employee): # Inherits setdata
    def displayName(self): # Changes display
        print('Current value = "%s"' % self.name)

dev1 = Developer()
dev1.name = 'Anju'
dev1.displayName()

class ThirdClass(Developer): # Inherit from Developer
    def __init__(self, value): # On "ThirdClass(value)"
        self.name = value
    def __add__(self, other): # On "self + other"
        return ThirdClass(self.name + other)
    def __str__(self): # On "print(self)", "str()"
        return '[ThirdClass: %s]' % self.name

a = ThirdClass('Selin') # __init__ called
a.displayName() # Inherited method called
print(a) # __str__: returns display string
b = a + ' rocks' # __add__: makes a new instance
b.displayName() # b has all ThirdClass methods
print(b) # __str__: returns display string

ThirdClass.displayName(a) # shows Selin