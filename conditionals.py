if True:
    print("Conditional was True")
if False:  # will not print
    print("Conditional was true")

language = "Lua"

# Comparison
# Equal:              ==
# Not Equal:          !=
# Greater than:       >
# Lesser Than:        <
# Greater or Equal    >=
# Lesser or equal     <=
# Object Identity     is

if language == "Python":
    print("This is Python")
elif language == "Java":
    print("This is Java")
elif language == "JavaScript":
    print("This is JavaScript")
else:
    print(f"Non-Existent: {language} is a new programming language.")

# Boolean operations
# and
# or
# not

user = "Admin"
logged_in = False

if user == "Admin" and logged_in:
    print("Welcome Admin")
else:
    print("Access Denied!")

# or - only one needs to be true
if user == "Admin" and logged_in:
    print("Welcome Admin")
else:
    print("Access Denied!")

# not - changes the boolean
if not logged_in:
    print("Please Log In")
else:
    print("Welcome")

# object id (is)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)  # false.. 2 different objects in memory
print(a is c)  # true.. shares same memory
# how to test it
print(id(a))
print(id(b))
print(id(c))

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), []
# Any empty mapping. For example , {}


# function not to repeat the code for condition
def condition(condition):
    if condition:
        print("Evaluated to True")
    else:
        print("Evaluated to False")


condition(False)
condition(None)
# numbers
condition(0)
condition(2)  # true
# squencing - empty means false
condition("")
condition(())
condition([])
# mapping - empty also is false
condition({})
