# OVERRIDING (GOOD) AND POLYMORPHISM 
# https://www.geeksforgeeks.org/polymorphism-in-python/
# MULTIPLE INHERITANCE (GOOD) and POLYMORPHISM (GOOD)
# https://overiq.com/python-101/inheritance-and-polymorphism-in-python/

# Parent Foo class
class Foo:
    def __init__(self, val):
        self.val = val
    def printVal(self):
        print(self.val)

# Simple inheritance of Foo class by DerivedFoo
class DerivedFoo(Foo):
    def negateVal(self):
        self.val = -self.val

obj1 = DerivedFoo(12)
obj1.negateVal()
obj1.printVal()
obj1.negateVal()
obj1.printVal()

# isinstance is an instance of Foo class
print(isinstance(obj1, Foo))

# issubclass function below checks if DerivedFoo is an inherited class of Foo
print(issubclass(DerivedFoo, Foo))
