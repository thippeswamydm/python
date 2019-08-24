# Describe usage of 'global' key
# 'global' key is used to reference a variable usage in 
#       global context within a local scope

def spam():
    global eggs
    print(eggs) # Complains of "Using variable 'eggs' before assignment"
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)