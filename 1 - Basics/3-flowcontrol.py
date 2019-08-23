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
