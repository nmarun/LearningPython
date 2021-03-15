# Lists and Dictionaries
rge = range(-4, 4);
list(rge);

names = ["Pallavi", "Aryan", "Ayush", "Arun"];
# since append and sort are changed in-place, the return of these methods is 'None'
# you'll lose the reference to the list if you do this
names = names.sort(key = str.lower);
print(names);

states = ["KA", "HP", "AP", "GJ"];
# remove items
del states[2];
states;
del states[2:];
states;

dictionary = {'spam': 2, 'ham': 1, 'eggs': 3};
type(dictionary.keys);