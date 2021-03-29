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

import imp
imp.reload(Module1)
imp.reload(Module2)
