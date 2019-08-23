# parent class with printVal function
# https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes

class Foo:
    def __init__(self, val):
        self.__val = val
    def printVal(self):
        print(self.__val)

# overrides printVal of Foo into its own implementation
class DerivedFoo2(Foo):
    def supersVal(self):
        print('My value is %s' % self.__val)

obj1 = DerivedFoo2(12)
obj1.printVal()
obj1.supersVal()

# Traceback (most recent call last):
#   File "70-classes-private-variable-access.py", line 15, in <module>
#     obj1.supersVal()
#   File "70-classes-private-variable-access.py", line 11, in supersVal
#     print('My value is %s' % self.__val)
# AttributeError: 'DerivedFoo2' object has no attribute '_DerivedFoo2__val'