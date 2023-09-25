from loop_iterate import divider


def _hello_func():
    pass  # prevent error on empty function


print(_hello_func())  # function executed if it has ()
print(_hello_func)  # does not execute.. shows memory location

# repeated...
print("Hello Function!!!")
print("Hello Function!!!")
print("Hello Function!!!")
print("Hello Function!!!")
print("Hello Function!!!")


def hello_func():
    print("Hello Function!!")


# Keep code DRY - don't repeat yourself
hello_func()
hello_func()
hello_func()
hello_func()
hello_func()


def r_hello_func():
    return "Hello Function 🐍"


divider()

r_hello_func()  # not printing
print(r_hello_func())
print(r_hello_func().upper())


# passing arguments to functions
def greetings(name):
    return f"Hi {name}!"


print(greetings("Anthony"))


# passing arguments to functions, with optional funct
def greeting(greet, name="You"):
    return f"{greet}, {name}!"


print(greeting("Hi"))
print(greeting("Hello", "Anthony"))

####################
# kwargs


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


divider()

student_info("Math", "Art", name="John", age=22)

divider()
# list of courses
courses = ["Math", "Art"]
info = {"name": "John", "age": 22}

student_info(courses, info)
divider()
student_info(*courses, **info)
