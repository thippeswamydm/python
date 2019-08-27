# Describes scope rules in terms of local and global
# Assignation of variables inside a local scope makes the variable
#     locally scoped, even if a global variable is available in the global scope


def spam():
    global eggs
    eggs = 'spam'  # this is the global


def bacon():
    eggs = 'bacon'  # this is a local


def ham():
    print(eggs)  # this is the global since there is no assignment


eggs = 42  # this is the global
spam()
print(eggs)  # prints spam since is global
bacon()
print(eggs)
# prints spam since bacon implements local variable and doesnt effect eggs variable
