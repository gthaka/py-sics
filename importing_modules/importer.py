import my_module as mm  # access everything else iin the module
from my_module import find_index, test  # access only specified module

# one of the place python searches for modules is sys.path
import sys

# from my_module import * # not clear

courses = ["History", "Math", "Art", "Music", "CompSci"]

# index = my_module.find_index(courses, "Math")
index = mm.find_index(courses, "Math")
print(index)

# specific
index2 = find_index(courses, "CompSci")
print(index2)
print(test)

############################################
# sys.path dir list is as follow
# 1. current dir of this script that is running
# 2. python path env varible
# 3. standard lib dir
# 4. site path directory for 3rd party libraries
print(sys.path)


# what if we have modules outside this dir
# one way is to define where the module is
import getpass
import os

# specific to my localpath
# sys.path.append(f"/home/{getpass.getuser()}/dev/pythonland/py-sics")
# parent_dir = os.path.dirname(os.getcwd())
parent_dir = os.getcwd()
print(parent_dir)
sys.path.append(parent_dir)
from module_outside import out_test

print(out_test)
