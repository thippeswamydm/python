# Describe using of Error Handling of code in python
# except blocks can be named
# You can have or handle multiple except errorhandlers
#       and executing the same except codes
#           Example
#           except (Err1, Err2, Err3):
# try...except...finally can be used to trigger finally a block irrespective
#       of whether an error occured or not


def obj(divideBy):
    return 42 / divideBy


try:
    print(obj(2))
    print(obj(12))
    print(obj(0))
    print(obj(1))
except ZeroDivisionError:  # Catch specific error
    print('Error: Invalid argument.')
finally:
    print('Finally Triggered.')

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
