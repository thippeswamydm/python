# Declaring a local variable inside a local scope of a function
# locallly scoped variables cannot be accessed outside 
#       the local scope; in this case the function
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

def name():
    eggs = 10
print(eggs)