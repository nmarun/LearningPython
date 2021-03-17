# Assignments, Expressions, and Prints

# tuple assignment positional
one, two = '1', '2'
print(one)
print(two)

# list assignment positional
[spam, ham] = ['yum', 'YUM']
print(spam)
print(ham)

# string length should match the number of variables
# else throws 'too many values to unpack (expected 4)' error
a, b, c, d = 'spam' # Sequence assignment, generalized
a, b, c, d # shows ('s', 'p', 'a', 'm')
e, *f = 'spam' # Extended sequence unpacking
e, f # shows ('s', ['p', 'a', 'm'])