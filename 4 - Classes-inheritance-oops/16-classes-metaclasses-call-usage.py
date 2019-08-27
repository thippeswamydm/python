# Describes how to add attributes to a metaclass or re-implement the type __call__ methods

# /opt/pycharm/pycharm-community-2019.2.1/bin# sh pycharm.sh
# Concept taken from following
# https://github.com/django/django/blob/master/django/db/models/base.py

class ModelBase(type):
    def hello(cls):
        print("Test", type(cls))

    def __init__(cls, name, bases, dct):
        print('bases', bases)
        print('name', name)
        print('dict', dct)
        print('cls.__dict__', cls.__dict__)
        return super(ModelBase, cls).__init__(cls)

    def __call__(self, *args, **kwargs):
        setattr(self, "hello", self.hello)
        setattr(self, "sayHello", self.hello)
        return super(ModelBase, self).__call__()

class MyTest(metaclass=ModelBase):
        def testhello(self):
            self.sayHello()


obj = MyTest()
obj.sayHello()
obj.testhello()

