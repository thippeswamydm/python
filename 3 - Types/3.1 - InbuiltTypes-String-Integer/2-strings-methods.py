# Describes string manipulation, methods available, and it details
# len() is an inbuilt function that gives the number of characters in a string
#       since string behaves like a iterator

name = "I am a string which is a list of characters joined together"

# length of string list OR number of characters
print(len(name))

# Capitalize string
print(name.capitalize())

# String to lowercase
print(name.lower())

# Make string caseless for comparision
print(name.casefold() == name.casefold())

# Count the number of characters
print(name.count('s',0,len(name)))

# Encode a string value to a different encoding
# 'strict' or 'ignore' or 'replace' alternate errors value
print(name.encode(encoding="utf8", errors="strict"))

# Find a character or phrase
print(name.find("s", 0, len(name)))

# Return the index of the first matching item
print(name.index("s"))

# Checks if string is numeric
print(name.isnumeric())

# Checks if string are all alphabets
print(name.isalpha())

# Checks if string is alpha numeric
print(name.isalnum())

# Checks if string is a decimal
print(name.isdecimal())

# Checks if string is a digit
print(name.isdigit())

# Checks if string is a valid identifier according to language
print(name.isidentifier())

# Checks if string is upper case
print(name.islower())

# Checks if string is lower case
print(name.isupper())

# Checks if string is title cased - capitalized first character of word
print(name.istitle())

# Checks if all characters are whitespace
print(name.isspace())

# Checks if printable
# if empty space then false
print(name.isprintable())

# Join function joins all the iterable items into a string
print(name.join(name.split("string", maxsplit=-1)))

# Split using provided delimiter
# maxsplit mentioned is optional and default is all
#   else splits based the number of counts
print(name.split("string", maxsplit=-1))

# Removes characters
# Strip of leading white spaces
print(name.lstrip())

# count is optional and if not provided will remove all
# print(name.replace(old, new, count))
print(name.replace("string", "s.t.r.i.n.g", -1))

# returns highest index if there are a number of string words
# start (2nd arg) and end (3rd arg) are optional
print(name.rfind("string", 0, len(name)))

# returns highest index if there are a number of string words
# start (2nd arg) and end (3rd arg) are optional
# Raises error if substring not found
print(name.rindex("string"))

# Removes characters
# Strip of trailing white spaces
print(name.rstrip("string"))
