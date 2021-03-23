# documentation interlude

class docstrings:
    """
    Module documentation 
    Words Go Here
    """

    spam = 40
    def square(x):
        """
        function documentation
        area of a square
        """
        return x ** 2 # square

    class Employee:
        "class documentation"
        pass
    print(square(4))
    print(square.__doc__)

print(docstrings.__doc__)
print(docstrings.square.__doc__)
print(docstrings.Employee.__doc__)
