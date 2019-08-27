# Describes type of error when method of list or one type used on another

eggs = 'hello'
eggs.append('world')

# ERROR DETAILS - 
# Traceback (most recent call last):
#   File "<pyshell#19>", line 1, in <module>
    # eggs.append('world')
# AttributeError: 'str' object has no attribute 'append'
