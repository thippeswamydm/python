# Difference between a property and attribute - Classes
# https://stackoverflow.com/questions/7374748/whats-the-difference-between-a-python-property-and-attribute

# Properties - functions
# https://docs.python.org/3/library/functions.html#property
# In Python:
# Attribute is variable
# Property is variable with getter and setter method
# Method is class function

# Internet says attributes and properties are interchangable 
# and methods are seperate class functions
class C:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

# If c is an instance of C, 
# c.x will invoke the getter, 
# c.x = value will invoke the setter and 
# del c.x the deleter
