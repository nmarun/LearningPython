# Scopes

a = 13
b = 2
def times(x, y):
    x = x+1 # this change is on a local copy
    return x*y

times(a, b) # shows 28
a # still shows 13

X = 88 # Global X
def func():
    global X
    X = 99 # Global X: outside def
    print(X)

func()
print(X) # Prints 99

# closure
def f1():
    X = 88
    def f2():
        print(X) # Remembers X in enclosing def scope
        return f2 # Return f2 but don't call it
action = f1() # Make, return function
action() # Call it now: prints 88

# Enclosing scopes are often employed by the lambda function-creation expressions
def maker(N):
    N+=1
    return lambda X: X ** N # lambda functions retain state too

h = maker(3)
h(2) # 4 ** 4, not 4 ** 3 because of the N+=1 
