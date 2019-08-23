# Difference between a property and attribute
# https://stackoverflow.com/questions/7374748/whats-the-difference-between-a-python-property-and-attribute

# Attribute is variable
# Property is variable with getter and "setter method"
# Method is class function

# Internet says attributes and properties are interchangable 
# and methods are seperate class functions
class A(object):
    _x = 0
    '''A._x is an attribute'''

    @property
    def x(self):
        '''
        A.x is a property
        This is the getter method
        '''
        return self._x

    @x.setter
    def x(self, value):
        """
        This is the setter method
        where I can check it's not assigned a value < 0
        """
        if value < 0:
            raise ValueError("Must be >= 0")
        self._x = value

a = A()
a._x = -1
a.x = -1
# Correct one
# a.x = 1
print(a.x)