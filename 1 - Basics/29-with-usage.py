# Describes the usage of `with` statement

# USAGE
# with obj as aliasname:
#   executionstatement

# open is a function that opens a file using default utf8 encoding
with open("exercises.txt", "r") as fh:
    long_description = fh.read()
print(long_description)

