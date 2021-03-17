# Introducing Statements

import random

count = 0
while count <5:

    rnd = random.random()
    count += 1

    if(rnd < 0.25):
        print("first quarter")
    elif(rnd < 0.5):
        print("second quarter")
    elif(rnd < 0.75):
        print("third quarter")
    else:
        print("fourth quarter")

