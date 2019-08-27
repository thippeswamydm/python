# Describes how to add attributes to a metaclass or re-implement the type methods/properties

# Concept taken from following
# https://github.com/django/django/blob/master/django/db/models/base.py

# Creating a metaclass extending type
class UpperAttrMetaclass(type):

    someValue = "My public someValue attribute from Custom meta UpperAttrMetaclass"
    __privateValue = "My private attribute from Custom meta UpperAttrMetaclass"

    def common_attribute_def(cls):
        print("Printing from a UpperAttrMetaclass.common_attribute_def to be added", cls.__hash__(cls))

    def second_attribute_def(cls):
        print("Printing from a UpperAttrMetaclass.second_attribute_def to be added", cls.__hash__(cls))

    def __init__(cls, clsname, bases, dct):
        print("Initialising my init from __init__", cls.__hash__(cls))
        setattr(cls, 'common_attribute_def', cls.common_attribute_def)
        return super(UpperAttrMetaclass, cls).__init__(cls)

    def __call__(cls, *args, **kwargs):
        print('args, kwargs from __call__', args, kwargs)
        setattr(cls, "second_attribute_def", cls.second_attribute_def)
        setattr(cls, "someValue", cls.someValue)
        setattr(cls, "__privateValue", cls.__privateValue)
        return super(UpperAttrMetaclass, cls).__call__()

    def __new__(cls, clsname, bases, dct):
        uppercase_attr = {}
        print('Printing bases from type base class: __new__', bases)
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        # Following code does not add the attribute to the class derived from the metaclass
        # setattr(cls, 'common_attribute_def', cls.common_attribute_def)
        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

# Creating base class for a sample bases in meta class defs
class BaseClassTwo:
    def mybasetwo(self):
        print("Extended: In mybasetwo function from BaseClassTwo")

# Creating base class for a sample bases in meta class defs
class BaseClass:
    def mybase(self):
        print("Extended: In mybase function from BaseClass")

# Creating MyNewsClass extending two base classes and using a meta class defined above
class MyNewsClass(BaseClass, BaseClassTwo, metaclass = UpperAttrMetaclass):
    # Defining the __init__ method
    def __int__(self):
        super()

    # defining a method MyNewClassDef
    def MyNewClassDef(self):
        print("Usage: small caps attributes due to metaclass new_fn from MyNewsClass")

obj = MyNewsClass()

# Checks for availability of methods
obj.MYNEWCLASSDEF()
obj.mybase()
obj.mybasetwo()
obj.common_attribute_def()
obj.second_attribute_def()
print(obj.someValue)
print(obj.__privateValue)
