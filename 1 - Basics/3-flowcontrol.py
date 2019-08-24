# Describes usage of if...elif...else statement
# USAGE
# if (conditions):
#   execution block
# elif (conditions):
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
