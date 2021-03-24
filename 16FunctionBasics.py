# Function basics

# arguments are type-insensitive
# allows for polymorphism
def times(x, y):
    return x*y

times(3, 4) # shows 12
times('a', 3) # shows 'aaa'
times([1, 2], 2) # shows [1, 2, 1, 2]