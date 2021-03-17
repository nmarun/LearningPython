
x = 3
y = 2
print(x / y)

name = 'Arun'
print(name[-3])

print(name[1:])
name = 'Pallavi'
# this is a comment

charArray = list(name)
charArray[1] = 'i'
print(charArray)

charArray[1] = "a"
print(charArray)
name.find("lla")
tempName = name
tempName.replace("lla", "all")
print(name)


"%s and %s" % ("ham", "eggs")
"{} and {}".format("ham", "eggs")

dir(name)

print('sp\xc4m') # unicode

isValid = False
if(isValid)
    print('valid')    
else
    print('invalid')

dictionary = {'a': 1, 'b': 2, 'c': 3}
dictionary['a']
keys = list(dictionary.keys())
keys.sort()
for key in keys:
    print(dictionary[key])

# sorts keys
for key in sorted(dictionary):
    print(key, '=>', dictionary[key])

# tuple
tuple = (1, 2, 3, 4);
len(tuple);

tuple[0];
tuple.index(3); # 0-based index

file = open("data.txt", "w");
file.write("Hello Py\n");
file.write("more Py\n");
file.close();

file = open("data.txt");
text = file.read();
print(text);
text.split();

for line in open("data.txt"):
    print(line);

class Employee:
    def __init__(self, name, pay):
        self.name = name;
        self.pay = pay;
    def lastName(self):
        return self.name.split()[-1];
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent);

bob = Employee("Bob Smith", 1000);
mary = Employee("Mary Jane", 2000);

bob.lastName();
bob.pay;
mary.giveRaise(0.2);
mary.pay;