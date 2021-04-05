# Advanced Class Topics

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)

a = Spam()
b = Spam()

Spam.printNumInstances()

# static and class methods
class Methods:
    def imeth(self, x): # Normal instance method: passed a self
        print([self, x])
    def smeth(x): # Static: no instance passed
        print([x])
    def cmeth(cls, x): # Class: gets class, not instance
        print([cls, x])
    smeth = staticmethod(smeth) # Make smeth a static method (or @: ahead)
    cmeth = classmethod(cmeth) # Make cmeth a class method (or @: ahead)

obj = Methods()
obj.imeth(1) # shows [<__main__.Methods object at 0x0000025864617A00>, 1]
Methods.imeth(obj, 2) # shows [<__main__.Methods object at 0x0000025864617A00>, 1]

Methods.smeth(3) # shows 3
obj.smeth(4) # shows 3

Methods.cmeth(5) # shows [<class '__main__.Methods'>, 4]
obj.cmeth(6) # shows [<class '__main__.Methods'>, 4]

class Spam:
    numInstances = 0
    def count(cls): # Per-class instance counters
        cls.numInstances += 1 # cls is lowest class above instance
    def __init__(self):
        self.count() # Passes self.__class__ to count
    count = classmethod(count)
    def printCount(self):
        print(self.numInstances)
    printCount = staticmethod(printCount)

class Sub(Spam):
    numInstances = 0
    def __init__(self): # Redefines __init__
        Spam.__init__(self)

class Other(Sub): # Inherits __init__
    numInstances = 0

x = Spam()
y1, y2 = Sub(), Sub()
z1, z2, z3 = Other(), Other(), Other()

x.numInstances, y1.numInstances, z1.numInstances # shows (1, 2, 3)
Spam.numInstances, Sub.numInstances, Other.numInstances # shows (1, 2, 3)
