# Advanced Function Topics

# Recursion
def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:]) # Call myself recursively

list = [1, 2, 3]
mysum(list)

from functools import reduce

reduce((lambda x, y: x + y), [1, 2, 3, 4])
reduce((lambda x, y: x * y), [1, 2, 3, 4])