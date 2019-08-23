spam = ['cat', 'bat', 'rat', 'elephant']
spam[10000]

# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
    # spam[10000]
# IndexError: list index out of range

spam[int(1.0)]

# Traceback (most recent call last):
#   File "<pyshell#13>", line 1, in <module>
    # spam[1.0]
# TypeError: list indices must be integers, not float