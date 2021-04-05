# Exception Coding Details

dividend = 1
divisor = 0
try:
    dividend/divisor
except Exception as ex:
    print(ex)
    print(ex.args())
else:
    print("no exception occurred")
finally:
    print("finally.. it's over")

class TraceBlock:
    def divide(self, dividend, divisor):
        print(dividend/divisor)
    def multiply(self, multiplicand, multiplier):
        print(multiplicand*multiplier)
    def __enter__(self):
        print('starting with block')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('exception occurred! ' + str(exc_type))
            print(exc_value)
            print(exc_tb)
            return False # propagate the exception
            # return True # if exception is handled
            # not having the return statement would also propagate

if __name__ == '__main__':
    with TraceBlock() as action:
        action.divide(1, 2)
        # shows the below output
        # starting with block
        # 0.5
        # exited normally

    with TraceBlock() as action:
        action.multiply(1, 2)
        # shows the below output
        # starting with block
        # 2
        # exited normally

    with TraceBlock() as action:
        action.divide(1, 0)
        # shows the below output
        # starting with block
        # exception occurred! <class 'ZeroDivisionError'>
        # division by zero
        # <traceback object at 0x0000013CE98E8280>
        # Traceback (most recent call last):
        #   File "<stdin>", line 17, in <module>
        #   File "<stdin>", line 3, in divide
        # ZeroDivisionError: division by zero

