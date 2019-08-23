
class Foo:
    # Will not be accessible in the child class
    __test = None
    def __init__(self, val):
        self.val = val
    def printValFoo(self):
        print(self.val)
    # Will not be accessible in the child class
    def __printValFoo__(self):
        print(self.val)

class Foos:
    def __init__(self, val):
        self.val = val
    def printValFoos(self):
        print(self.val)

# Simple inheritance of Foo class by DerivedFoo
class DerivedFoo(Foo, Foos):
    def negateVal(self):
        self.val = -self.val

obj1 = DerivedFoo('test')
obj1.printValFoo()
obj1.printValFoos()