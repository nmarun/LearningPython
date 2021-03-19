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

#unpacking sequence
#unpack the list into variables
language=["hello","namaste","Bonjour","Konnichiwa"]
english,hindi,french,japanese=language
print("english={}, hindi={}, french={}, japanese={}".format(english,hindi,french,japanese))

nudge = 1
wink = 2
nudge, wink = wink, nudge # Tuples: swaps values
nudge, wink # Like T = nudge; nudge = wink; wink = T

print('hello world') # internally does the below
import sys 
sys.stdout.write('hello world\n')

import sys
temp = sys.stdout # Save for restoring later
sys.stdout = open('log.txt', 'a') # Redirect prints to a file
print('spam') # Prints go to file, not here
print(1, 2, 3)
sys.stdout.close() # Flush output to disk
sys.stdout = temp # Restore original stream
print('back here') # Prints show up here again
print(open('log.txt').read()) # Result of earlier prints

log = open('log.txt', 'a')
data = 'xyz'
print(data, file = log) # writing to file
log.close()
print(open('log.txt').read())