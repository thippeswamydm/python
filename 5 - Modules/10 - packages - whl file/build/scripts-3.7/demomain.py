# interpreter -> lib/pkgs/mod/file
import math
import sys
sys.path.append('./')
# > Pkg or pkgmodule (folder) > filemod > function/objs
from m import *
# from m.variables import *
# namespace
# __name__ > dont define > "__main__"
# __name__ = "myscript"
print("0-10-demo:", strvars.name)
print("0-10-demo:", type(printme), printme)
printme.funct(strvars.name)
print("0-10-demo:", math.sqrt(numvars.num))
print("0-10-demo:", __name__)

# Script
if __name__ == "__main__":
    print("0-10-demo:","Test Main")
if __name__ == "myscript":
    print("0-10-demo:", "Test myscript")


# from mod import *
# from mod import name, funct, num
# Scope for funct not imported
# from printme import name, num
# Import of folder using . notation
# Imports of modules/filemodules are explicit
# from m.printme import *
# from m.variables import *
# Alias names of modules
# from m import printme as pr
# from m import printme
# Module name and __name__ are different
# If __name__ is not defined then it will assign modname to __name__ when importing
#     name is defined in the imported file __name__ will be different from mod name
# If __name__ is not defined in the main script file
#       then it will assign __main__ to main script file
# from m import printme
# from m import printme, variables
# from m.variables import *
# Name collisions
