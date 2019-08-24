# Describe using of Error Handling of code in python
# try...except is used for error handling
# except can use a named error
# except without name will handle and execute if any error occurs

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
    except:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))