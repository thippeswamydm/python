# Single return value from function
def hello(name):
  print('Howdy! ' + name)
  return name
sing = hello('Testing Single Return')
print(sing)

# Multiple return from function
def helloMultiple(name):
  print('Howdy! ' + name)
  return 'name', name
mul = hello('Testing Multiple returns')
print(mul)