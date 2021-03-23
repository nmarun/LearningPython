# iterations and list comprehensions

# list comprehension
list = [1, 2, 3]
list = [x + 10 for x in list]
list # shows [11, 12, 13]

# nested comprehension
group1 = 'ab'
group2 = 'zy'

combinedList = [a + b for a in group1 for b in group2 ]
combinedList # shows ['az', 'ay', 'bz', 'by']

rng = range(10)
rng
iterator = iter(rng)
rng[0]
rng[-1]
iterator.__next__() # does not impact the index though we've subscripted ([]) above
next(iterator)
