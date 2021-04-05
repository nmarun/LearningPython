# Designing with Exceptions

import traceback
def inverse(x):
    return 1 / x
try:
    inverse(0)
except Exception:
    # uses sys.exc_info data
    traceback.print_exc(file=open('output.exc', 'w'))
    print('Bye')

file = open("output.exc", "r")
line = file.read()
print(line)
file.close()