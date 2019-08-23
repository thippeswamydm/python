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
