# Describes usage of if...elif...else statement
# 'if' key has to have a condition that returns a Boolean value
# 'if' key can also be followed by a boolean directly
# A condition checks for euality of two values or variables
# 'else' does not have a condition and executes if any above 'if' or 'elif' statements fails

# USAGE
# if (conditions):
#   execution block
# elif conditions:
#   execution block
# else:
#   execution block

name = input()
password = input()
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
    elif (password == 'alternate'):
        print('else if block alternate password')
    else:
        print('Wrong password.')
