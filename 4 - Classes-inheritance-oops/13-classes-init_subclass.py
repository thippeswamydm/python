# Describes usage of __init_subclass__ method

# # Variation
# # https://docs.python.org/3/reference/datamodel.html#implementing-descriptors
# class Philosopher:
#     def __init_subclass__(cls, default_name, **kwargs):
#         super().__init_subclass__(**kwargs)
#         cls.default_name = default_name

# class AustralianPhilosopher(Philosopher, default_name="Bruce"):
#     pass

# Sample codes
# https://gist.github.com/pjeby/75ca26f8d2a7a0c68e30

# VARIATION2 - Accessing superparent variable
# https://stackoverflow.com/questions/53189980/accessing-superparent-class-variable-in-python
# VARIATION3 - Static methods
# https://stackabuse.com/object-oriented-programming-in-python/

class WheelType:
    __type = "round"
    def __init__(self, val):
        self.__type = val
    def __init_subclass__(self, wType, **kwargs):
            super().__init_subclass__(**kwargs)
            self.__type = wType
            print('**kwargs WT',kwargs)
    def get_wheel_type(self):
        return self.__type
    def set_wheel_type(self, prop):
        self.__type = prop

class EngineType:
    __engineType = "jeep"
    def __init_subclass__(self, eType, **kwargs):
        super().__init_subclass__(**kwargs)
        self.__engineType = eType
        print('**kwargs ET',kwargs)
    def __init__(self, val):
        self.__engineType = val
    def getEngineType(self):
        return self.__engineType
    def setEngineType(self, val):
        self.__engineType = val

class Vehicle(EngineType, WheelType, eType="Test", wType="Tester"):
    __otherParts = ["bonet", "dicky", "rooftop"]
    __pendingParts = ["seats", "stearing"]
    def __init__(self, ppart, eType, wType):
        # When you have one Parent or Base class
        # super().__init__(eType)

        # When you have multiple Base or Parent class, pass arguments
        # EngineType.__init__(self, eType)
        # WheelType.__init__(self, wType)
        
        self.eType = eType
        self.__pendingParts.append(ppart)
    def set_pendingParts(self, val):
        self.__pendingParts = val
    def get_pendingPats(self):
        return self.__pendingParts
    def get_vehicle(self):
        return self.getEngineType(), self.__otherParts, self.__pendingParts
    def set_vehicle(self, et, oParts, pParts):
        self.setEngineType(et)
        self.__otherParts = oParts
        self.__pendingParts = pParts

vh = Vehicle("pPart", "Car","Square")
print(vh.getEngineType())
print(vh.get_wheel_type())