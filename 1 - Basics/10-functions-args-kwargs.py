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