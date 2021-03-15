x = 2; 
y = 3;
z = 4;

# y evaluated only once
x < y < z;

1.1 + 2.2 == 3.3;

# floor division
x // y;
7 // 3;

# closest number below value
import math;
math.floor(2.5);
math.floor(-2.5);

5//2;
-5//2;

whatType = (5/2), (6/-3);
type(whatType);
type(x);

# complex numbers; represented with a j or J
1j*1J;

(3+2j) * (5+3j);

import random;
random.random();
random.choice(["first", "second", "third"]);

suits = ['hearts', 'clubs', 'diamonds', 'spades'];
random.shuffle(suits);
suits;

# from [module] import [class]
from decimal import Decimal;
Decimal("0.1");

from fractions import Fraction;
x = Fraction(1, 5);
y = Fraction(2, 3);
print(x + y);

Fraction("0.234");

L = [1, 2, 1, 3, 2, 4, 5]
set(L)
L = list(set(L)) # Remove duplicates
L

set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]) # Find list differences
set('abcdefg') - set('abdghij') # Find string differences
set('spam') - set(['h', 'a', 'm']) # Find differences, mixed

engineers = {"bob", "sue", "ann", "vic"};
managers = {"tom", "sue"};
"bob" in engineers; # Is bob an engineer?
engineers & managers; # Who is both engineer and manager?
engineers | managers; # All people in either category
engineers - managers; # Engineers who are not managers
managers - engineers; # Managers who are not engineers
engineers > managers; # Are all managers engineers? (superset)
managers ^ engineers # Who is in one but not both?

#treats anything other than 0 as true
if (3-4):
    print("true");

a =3;
b = a;
a += 2;
# b still shows 3 and not 5
# immutable types cannot be changed in place
b;

list1 = [2, 3, 4];
list2 = list1;
list3 = list1[:]; # creates a new copy
list1[0] = 24;
list2; # shows [24, 3, 4], since lists are mutable types
list3; # remains unchanged
list1 == list2;
list1 == list3;
list1 is list2; #same values, same reference
list1 is list3; #same values; different reference

import sys;
sys.getrefcount(list1);
sys.getrefcount(list2);
sys.getrefcount(list3);