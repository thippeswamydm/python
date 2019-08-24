spam = {'name': 'Zophie', 'age': 7}
print('name' in spam.keys())
# True
print('Zophie' in spam.values())
# True
print('color' not in spam.keys())
# True
print('color' not in spam.keys())
# True
print('color' in spam) # 'color' in spam is essentially a shorter version of writing 'color' in spam.keys()
# False