# Describes usage of import statements and using a file as a import

# print module
# since it is imported into another file the __name__ is
#       assigned with the filename as __name__ value

# Defining printer
def printer():
    print('Print Module Called')

# Defining inputprinter
def inputprinter():
    print('Enter your name:')
    strs = input()
    print(str(strs))
