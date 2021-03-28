# Comprehensions and Generations

#scrambling
name = 'Arun'

def scramble(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]

scramble(name)
items = ['laptop', 'book', 'phone']
scramble(items)