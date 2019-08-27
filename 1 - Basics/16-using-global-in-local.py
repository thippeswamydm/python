# Describe usage of 'global' key
# 'global' key is used to reference a variable usage or definition in
#       global context within a local scope; whichever applies


def spam():
    global eggs
    print(eggs)
    # Linter Complains of "Using variable 'eggs' before assignment"
    # but code works
    eggs = 'spam'


eggs = 'global'
spam()
print(eggs)
