# Designing with classes

class Product:
    __name = "laptop"
    def __print(self):
        print(self.__name)

prod1 = Product()
# every class attribute that begins with __ and does not end with __,
#  gets its name mangled as _[className]__[attributeName]

prod1._Product__name # name mangling
prod1._Product__print()

class C1:
    def setInC1(self): self.__X = 88 # Now X is mine
    def printInC1(self): print(self.__X) # Becomes _C1__X in I

class C2:
    def setInC2(self): self.__X = 99 # Me too
    def printInC2(self): print(self.__X) # Becomes _C2__X in I

class C3(C1, C2): pass

I = C3() # Two X names in I
I.setInC1()
I.setInC2()
print(I.__dict__) # shows {'_C1__X': 88, '_C2__X': 99}
I.printInC1() # shows 88
I.printInC2() # shows 99

class Human:
    def printName(self, name): print(name)

human = Human()
human.printName('Elon') # bound method
Human.printName(human, 'Musk') # unbound method
# methods are called on an object, unlike functions
type(human.printName) # shows <class 'method'> 
type(Human.printName) # <class 'function'>
