# Describes how private variables are declared in a class

# Privacy is just a notion and denoted as following:
# __attribute refers to the fact that attribute is private
# The double '__' refers that it is private
# '__method__(self)' refers to the fact that method is private
# All private references donot stop us from accessing 
#       the private attriutes, properties, and methods

class Foo:
    __testPrivateVariableConvention = 1
    def __init__(self, val):
        self.__testPrivateVariableConvention = val
    def printVal(self):
        print(self.__testPrivateVariableConvention)
    def setVal(self, val):
        self.__testPrivateVariableConvention = val

test = Foo(12)
test.printVal()
test.setVal(3)
test.printVal()
# __testPrivateVariableConvention will not get set
test.__testPrivateVariableConvention = 4
test.printVal()