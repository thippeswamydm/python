# Describes how comparision identity operators are used
# Comparision Identity operators in a conditional expression checks for
#       two values OR
#       variable+value OR
#       variable+variable
# Returns boolean value

# Operation, Meaning
# is - object identity
# is not - negated object identity

name = "test"

if (type(name) is str):
    print('is operator', name, 1)

if name is None:
    print('is operator', name, 4)

if name is not int:
    print('is not operator', name, 4)
