# Tuples, Files and everything else

x = (40) # An integer!
type(x)

y = (40,) # A tuple containing an integer
type(y)

chap9File = open("chap9File.txt", "w");
chap9File.write('hello text file\n') # Write a line of text: string
chap9File.write('goodbye text file\n')
chap9File.close()

for line in open("chap9File.txt", "r"): # Use file iterators, not reads
    print(line, end=''); #end: string appended after the last value; default is newline
    print("line for every line"); # indentation makes it part of the "for" block
print("at last");

dictionary = {"a": 1, "b": 2}
datafile = open("datafile.pkl", "wb") # wb: write-binary
import pickle
pickle.dump(dictionary, datafile) # Pickle any object to file
datafile.close()

datafile = open("datafile.pkl", "rb") # rb: read-binary
content = pickle.load(datafile) # Load any object from file
content # shows {'a': 1, 'b': 2}
type(content) # shows <class 'dict'>

S1 = "spam";
S2 = "spam";
# short strings use the same reference
# Python caches for optimization
S1 == S2, S1 is S2; # hence shows (True, True)

S1 = "a longer string";
S2 = "a longer string";
S1 == S2, S1 is S2; # shows (True, False)

# absence of any special char
S1 = "alongerstring";
S2 = "alongerstring";
S1 == S2, S1 is S2; # shows (True, True)

# shared references point to the same memory location
L = [1, 2, 3]
M = ['X', L, 'Y'] # Embed a reference to L
M
L[1] = 0 # Changes M too
M # shows ['X', [1, 0, 3], 'Y']


L = [1, 2, 3]
M = ['X', L[:], 'Y'] # Embed a copy of L (or list(L), or L.copy())
L[1] = 0 # Changes only L, not M
L
M