# Describes the creation of globally scoped variable
# global scope variables are available to any scope
# Pass globally scoped variables as arguments for use within function, incase
#       you face a problem accessing globally scoped variables.
#       In such a case, it will be local scope and
#       will be reference of a variable within the function
# However, globally scoping behaviour changes as soon as there is a local assignation
# Check accessDifferenceOne and accessDifferenceTwo function


def accessGlobalVariableAsArgument():
    print(eggs)  # global scoped access of eggs since no assignation in function


eggs = 42
accessGlobalVariableAsArgument()
print(eggs)


def passGlobalVariableAsArgument(eggs):
    print(eggs)  # global scoped access of eggs since no assignation in function


eggs = 42
passGlobalVariableAsArgument(eggs)
print(eggs)


def accessDifferenceOne():
    eggs = 43  # Now locally scoped
    print(eggs)


eggs = 42
accessDifferenceOne()
print(eggs)


def accessDifferenceTwo(eggs):
    eggs = 43  # Now locally scoped and not global
    print(eggs)


eggs = 42
accessDifferenceTwo(eggs)
print(eggs)
