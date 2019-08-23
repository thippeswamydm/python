# the double __ means it is private
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