# Describe incorrect usage of multiple assignation which throws error

cat = ['fat', 'orange', 'loud']
size, color, disposition, name = cat

# ERROR DETAILS
# Traceback (most recent call last):
#   File "<pyshell#84>", line 1, in <module>
    # size, color, disposition, name = cat
# ValueError: need more than 3 values to unpack