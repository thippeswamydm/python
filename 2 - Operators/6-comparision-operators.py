# Operation, Meaning

# < - strictly less than
# <= - less than or equal
# > - strictly greater than
# >= - greater than or equal
# == - equal
# != not equal
# is - object identity
# is not - negated object identity

# check twovalues or variable+value or variable+variable
# return will be bool

class nam:
    name = 1

name = "test"
tester = nam()

# if (not name == "test"):
# if not type(name) == "str":
# if (name != "test"):

if (type(name) is str):
    print(name, 1)

if (isinstance(name, str) ):
    print(name, 2)

if (isinstance(tester, nam) ):
    print(repr(nam), 3)

if name is not int:
    print(name, 4)

