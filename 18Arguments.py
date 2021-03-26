# Arguments

def sum_all(*args): # *args converts arbitrary number of inputs into a tuple
    total = 0
    for val in args:
        total += val
    return total

arguments = 1, 2, 3, 4
sum_all(*arguments) # sending without the * would make the argument as a single tuple; 
