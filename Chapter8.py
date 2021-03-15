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

# sparse data structure
matrix = {};
matrix[(2, 3)] = "ab";
matrix[(6, 2)] = "zy";
matrix[(2, 3)];

#safer options to read from matrix
matrix.get((2, 3), 0); # Exists: fetch and return
matrix.get((2, 4), 0); # Doesn't exist: use default arg

keys = [1, 2, 3, 4];
values = ["a", "b", "c", "d"];
#zip function: combine separate lists of keys and values obtained dynamically at runtime
zipped = zip(keys, values);
dict(zipped);
