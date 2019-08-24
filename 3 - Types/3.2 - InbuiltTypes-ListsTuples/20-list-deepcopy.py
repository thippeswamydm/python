import copy

# copy copies the reference of lists inside the lists
spam = [[[7,8,9,0],2,3,4,5], 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[0][1] = 42
cheese[3] = 42
print(spam)
# ['A', 'B', 'C', 'D']
print(cheese)
# ['A', 42, 'C', 'D']
cheese[0][1] = 2

# deepcopy copies the lists inside the lists and not reference of the lists inside lists
cheeseDeepCopy = copy.deepcopy(spam)
print(spam)
print(cheeseDeepCopy)
# [[1,2,3,4,5], 'B', 'C', 'D']
cheeseDeepCopy[0][1] = 9
print(spam)
print(cheeseDeepCopy)
# [[1,9,3,4,5], 'B', 'C', 'D']