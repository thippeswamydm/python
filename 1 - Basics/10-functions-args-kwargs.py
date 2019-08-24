# Describes 
# passing of variables using arguments, 
# capturing all arguments as *args
# capturing all arguments as **kwargs

# Arguments can be passed to functions in definitions
# Arguments have to be compulsarily passed if declared in definition
# Arguments can be passed as named or unnamed arguments
# When name of argument is specified then it is referred to as keyword arguments
# Arguments can be of any type, can also be a function

def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Wonderland')

def printUnnamedArgs(*args):
    for x in enumerate(args):
        print(x)

printUnnamedArgs([1, 2, 3], [4, 5, 6])

def printKeyWordArgs(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

printKeyWordArgs(a=10, b=20)

def fncArgsKwargs(*args, **kwargs):
     print('ARGS: {} and KWARGS: {}'.format(args, kwargs))

fncArgsKwargs(1,2,3, a=1, b=2, c=3)