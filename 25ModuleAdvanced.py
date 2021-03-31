# Advanced Module Topics 

from Module1 import * # loads only non _x fields
_name # shows _name is not defined

import Module1
Module1._name

from dir1.Module4 import * # __all__ takes precedence over _x and loads __all__ names only
(a, b, _c, d) # shows b is not defined

from dir1.Module4 import a, b, _c, d # all other imports get every name
(a, b, _c, d) # shows ('name', 'place', 'animal', 'thing')

del a
(b, _c, d) # shows ('place', 'animal', 'thing')

import dir1.Module4
(a, b, _c, d) # shows ('name', 'place', 'animal', 'thing')
del dir1.Module4

