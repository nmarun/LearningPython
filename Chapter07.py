single = 'string';
double = "string";
triple = '''string'''; #escaped
triple2 = """string"""; #escaped

myfile = open(r'C:\new\text.dat', 'w') # turns off escape mechanism (\n, \t are treated as regular strings

name = "Arun";
name[1:-1];

alphabet = "abcdefghijklmnopqrstuvwxyz";
alphabet[1:10:2]; # Skipping items
alphabet[::2];

alphabet[::-1]; # reverse a string

alphabet.casefold();
alphabet.swapcase();

count = 12;
bigCount = 123456;
format = "count is %6d %-6d";
print(format % (count, count));
print(format % (bigCount, bigCount));

dictionary1 = {"qty": 1, "food": "fish"};
dictionary2 = {"qty": 2, "food": "fruits"};
list = [];
list.append(dictionary1);
list.append(dictionary2);
list;

vars();

import sys
# indexing helps reorder the variables - 1 first then 0
# 
'My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})

print('%s=%s' % ('spam', 42)) # Format expression: in all 2.X/3.X
print('{0}={1}'.format('spam', 42)) # Format method: in 3.0+ and 2.6+
print('{}={}'.format('spam', 42)) # With autonumbering: in 3.1+ and 2.7