# Describes usage of if...else statement
# input() is a inbuilt function that takes input from user in command line
# else statement is not compulsary. Only if statement needed
# Does not create a local scope of its own
# Takes scope of the level it is defined
# Creates a conditional block however
# USAGE
# if (condition):
#   execution block

name = input()
password = input()
if name == 'Mary':
  print('Hello Mary')
  if password == 'swordfish':
    print('Access granted.')
  else:
    print('Wrong password.')