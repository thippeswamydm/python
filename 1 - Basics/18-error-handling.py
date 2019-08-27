# Describes using of Error Handling of code in python
# try...except is used for error handling
# 'try' block will be be executed by default
# If an error occurs then the specific or related 'except' block will be trigered
#       depending on whether the 'except' block has named error or not
# 'except' can use a named error
# 'except' without name will handle and execute if any error occurs
# You can have any number of 'except' blocks


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
    except:
        print('Error: Invalid argument.')


print(spam(2))
print(spam(12))
# Will throw ZeroDivisionError and will be captured triggering respective except block
print(spam(0))
print(spam(1))
