# Describes how comparision operators are used
# Comparision operators in a conditional expression checks for
#       two values OR
#       variable+value OR
#       variable+variable
# Returns boolean value

# isinstance() is an inbuilt function that checks
#       if a object is an instance of specific type

# Operation, Meaning

# < - strictly less than
# <= - less than or equal
# > - strictly greater than
# >= - greater than or equal
# == - equal
# != not equal

# Basic class defintion to demostrate usage of operators


class nam:
    name = 1


name = "test"
tester = nam()

# Different usage of comparision operators
#       (in combination with boolean operators)

# if (not name == "test"):
# if not type(name) == "str":
# if not (name == "test"):
# if (name != "test"):

if (type(name) == 'str'):
    print(name, 1)

if (isinstance(name, str)):
    print(name, 2)

if (isinstance(tester, nam)):
    print(repr(nam), 3)

if ((isinstance(name, str) == True) or (not name == 'test')):
    print(name, 2)

if ((isinstance(name, str) == True) and not (name == 'test')):
    print(name, 2)
