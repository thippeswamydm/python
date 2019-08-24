# Describes a list and working with its elements
# List is a sequence, iterator that can contain any type of items in it
# A list can also have lists or tuples in them
# A list is mutable, which means its items can be changed or modified
# A list behaves like array of other programming language
# A list is created using [] or square brackets
# A list item can be referenced by a index and the indexing starts with 0/zero
# A list can be iterated or looped using 'for' or 'while' loops


# Simple list created using [] brackets
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
print(spam[1]) # 'bat'
print(spam[-1]) # 'elephant'

nums = [1,2,3,4,5]
print(nums)

print(nums[0]) # 1
print(nums[-1]) # 5

print(spam[1:4]) # [bat', 'rat']
print(spam[:4]) # ['cat', 'bat', 'rat']
print(spam[1:]) # [bat', 'rat', 'elephant']

listOfLIsts = [['cat', 'bat', 'rat', 'elephant'], [1,2,3,4,5]]

print(listOfLIsts[0][1]) # 'bat'
print(listOfLIsts[1][1]) # 2

print(len(spam))
print(len(nums))
