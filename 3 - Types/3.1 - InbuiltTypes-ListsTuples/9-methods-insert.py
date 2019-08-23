spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)
spam.insert(-1, 'testsecondlastend')
print(spam)
spam.insert(len(spam), 'testend')
print(spam)