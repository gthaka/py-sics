message = "Hello Snakes 🐍"
print(message)

# multiline string
message = """I was to see if THIS can run in 
multiple lines 🤔"""
print(message)

# length of string
print(len(message))

# location using index
print(message[len(message) - 1])

# slicing
print(message[0:5])
print(message[:6])
print(message[1:])

# lower and upp
print(message.lower())
print(message.upper())

# count certain characters or string
print(message.count("o"))
# get the index position
print(message.find("multiple"))

# replace
new_message = message.replace("THIS", "this 👇🏽")
print(new_message)

################################################
greeting = "Hello"
name = "Anthony"

message = greeting + ", " + name + "🙋🏽‍♂️"
print(message)

# formatted string
message = "{}, {}. Welcome!".format(greeting, name)
print(message)

# py >3.6
message = f"{greeting}, {name.upper()}. Welcome!"
print(message)

# shows attributes and methods avaible
print(dir(name))

# more detailed info
# print(help(str))
print(help(str.lower))
