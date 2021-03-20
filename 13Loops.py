# while and for loops

x = 'spam'
while x: # While x is not empty
    print(x, end=' ') # In 2.X use print x,
    x = x[1:] # Strip first character off x

while test:
    statements
    if test: break # Exit loop now, skip else if present
    if test: continue # Go to top of loop now, to test1
else:
    statements # Run if we didn't hit a 'break'

import math
y = 13
x = math.ceil(math.sqrt(y)) # For some y > 1
x
while x > 1:
    if y % x == 0: # Remainder
        print(y, 'has factor', x)
        break # Skip else
    x -= 1
else: # Normal exit
    print(y, 'is prime')

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T: # Tuple assignment at work
    print(a, b)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
zipped = zip(list1, list2)
list(zipped)

keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]
dictionary = {}
for (k, v) in zip(keys, vals): 
    dictionary[k] = v

print(dictionary)

name = 'Arun'
enum = enumerate(name)
enum # shows <enumerate object at [some memory location]>
next(enum) # shows (0, 'A')
next(enum) # shows (1, 'r')
next(enum) # shows (2, 'u')