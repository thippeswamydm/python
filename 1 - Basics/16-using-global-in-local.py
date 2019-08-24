# Describe usage of 'global' key
# 'global' key is used to reference a variable usage in 
#       global context within a local scope

def spam():
    global eggs
    print(eggs) # Linter Complains of "Using variable 'eggs' before assignment" but code works
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)