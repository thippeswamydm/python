name = ''
age = 0
while (not name) or (not age) or (age == 0):
    if (name and age == 0): 
        print('Please enter your age ')
        age = input()
    if (not name):
        print('Enter a new name')
        name = input()
    if (age): print('Hello ' + str(name) + ', your age is ' + str(age))
    else: print('Hello ' + str(name))
print('Finished loop')