def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError: # Catch specific error
    print('Error: Invalid argument.')

    # try:
    #    # do something
    #    pass
    # except ValueError:
    #    # handle ValueError exception
    #    pass
    # except (TypeError, ZeroDivisionError):
    #    # handle multiple exceptions
    #    # TypeError and ZeroDivisionError
    #    pass
    # except:
    #    # handle all other exceptions
    #    pass
    # finally:
    #     pass

