# Allows us to work with key-value pairs
# keys can be different datatypes

student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
print(student)
# get a value based on a key
print(student["courses"])
# to prevent a KeyError for non existent key can use .get
print(student.get("phone"))
# print(student.get("phone", "Not Found"))  # can return a default if None
# ^^ the above line seems to break the code from execution.

# we can add a key to the dict
student["phone"] = "+254700112233"
student["name"] = "Jane"
print(student)

# update multiple values at a time
student.update({"name": "Scott", "age": 27, "phone": "11223344", "gender": "F"})
print(student)

del student["gender"]
print(student)

# pop removes and return the value
age = student.pop("age")
print(age)

# number of keys we have
print(len(student))

# get keys and values
print(student.items())
print(student.keys())
print(student.values())

# loop through keys
for key in student:
    print(key)

# loop through keys & values
for key, value in student.items():
    print(key, value)
