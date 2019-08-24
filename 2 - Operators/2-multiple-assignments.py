# Describes how multiple assignment works
# Works on sequences, etc
# The number of variables have to be same as number of items
# This is referred to as destructuring
# Destructuring also applies to function multiple return values which return tuple

cat = ['fat', 'orange', 'loud']
size, color, disposition = cat


# Multiple return from function
def helloMultiple(name):
  print('Howdy! ' + name)
  return 'name', name
var1, var2 = helloMultiple('Testing Multiple returns captured in multiple values')
print(var1, var2) 