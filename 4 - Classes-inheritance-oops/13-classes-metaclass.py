
# 3.3.3.1. Metaclasses
# https://docs.python.org/3/reference/datamodel.html#metaclasses
# The potential uses for metaclasses are boundless. 
# Some ideas that have been explored include 
# enum, logging, interface checking, automatic delegation, 
# automatic property creation, proxies, frameworks, 
# and automatic resource locking/synchronization.
# Look at documentation

# Sample codes
# https://gist.github.com/pjeby/75ca26f8d2a7a0c68e30

# Describes Meta and __call__ magic methods
# https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/

# CREATING CLASS DIRECTLY USING TYPE
# >>> MyClass = type('MyClass', (), {})
# >>> MyClass
# <class '__main__.MyClass'>

class Meta(type):
    pass

class MyClass(metaclass=Meta):
    def test(self):
        print("My test")

class MySubclass(MyClass):
    def tester(self):
        print("My tester")

obj = MySubclass()
