# Describes how boolean operators are used
# 'and', 'or', and 'not' keys are boolean operators
# works on boolean values and returns boolean values
# (condition) and (condition)
# (condition) or (condition)
# (not condition) and (condition)

name = "test"

# Different usages of 'not' key
# 'not' key is a checker that checks for inverse of result
#       of condition or boolean representation of a variable/value
# 'not' key returns a boolean value

# if (not name == "test"):
# if not type(name) == "str":
# if not (name == "test"):
# if (name != "test"):
if not name:
    print(name, 4)

if (type(name) is str):
    print(name, 1)

if (isinstance(name, str) and (not name)):
    print(name, 2)

# 'and' key will allow getting into the block only if both conditions return True
# 'and' key has precendence for Falsy value
if (isinstance(name, str) and (not name == 'test')):
    print(name, 2)

# 'or' key will allow getting into the block if either one returns True
# 'or' key has precendence for Thruthy value
if (isinstance(name, str) or (not name == 'test')):
    print(name, 2)
