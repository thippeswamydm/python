# Describes difference between interpretation difference between global and local scope
# Globally scoping behaviour changes as soon as there is a local assignation
# Check accessDifferenceOne and accessDifferenceTwo function

def globalSpam():
        print(eggs) # prints 'spam global'

def locallyScoped():
        eggs = 'spam local'
        print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    globalSpam()
    locallyScoped()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'

def accessDifferenceThree():
    print(eggs) # Complains of "UnboundLocalError:" mentioning using variable 'eggs' before assignment"
    eggs = 43 
    # Will throw error since print is done before assignation
    # of value to locally scoped variable
eggs = 42
accessDifferenceThree()

# Traceback (most recent call last):
#   File "15-local-global-variable-usage.py", line 29, in <module>
#     accessDifferenceThree()
#   File "15-local-global-variable-usage.py", line 24, in accessDifferenceThree
#     print(eggs) # Complains of "Using variable 'eggs' before assignment"
# UnboundLocalError: local variable 'eggs' referenced before assignment

print(eggs)
