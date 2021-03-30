# Modules - Coding

import Module1 # Get module as a whole (one or more)
Module1.printer("Hello world!") # Qualify to get names
del Module1
Module1.printer("Hello world!") # shows error: Module1 not defined

from Module1 import printer # Copy out a variable (one or more)
printer('Hello world!') # No need to qualify name
del Module1 # Module1 not needed as printer is pointing to Module1.printer
printer('Hello world!') # still works

from Module1 import * # Copy out _all_ variables; used only at the top level module file and not within a function
printer('Hello world!')
del Module1
printer('Hello world!') # still works

del Module1
del Module2

from Module1 import printer
from Module2 import printer # overwrites the one fetched from Module1
printer("some text") # calls Module2.printer()

import Module2
list(Module2.__dict__.keys())
Module2.__dict__.get('__name__')

list(name for name in Module2.__dict__.keys() if not name.startswith('__')) 
# uses list comprehension
# shows ['printer', 'printer2']
list(name for name in Module2.__dict__ if not name.startswith('__')) 
# uses generator 
# shows ['printer', 'printer2']

# module nesting
import Module1
Module1.Module2.printer("module nesting")
type(Module1.Module2) # shows <class 'module'>

import imp
imp.reload(Module1)
imp.reload(Module2)

imp.reload(Module2)
from Module2 import printer3
printer3() # still refers to the previous version of printer3() and is not affected by the reload
