# Lists -> sequencial data
default_courses = ["History", "Math", "Pysics", "CompSci"]
courses = ["History", "Math", "Pysics", "CompSci"]
print(courses)
print(len(courses))
# access via index
print(courses[0])
# print(courses[len(courses) - 1])
print(courses[-1])
# range of values access
print(
    courses[0:2]
)  # first index is inclusive, but second is not index 0 and 1 but not 2
print(courses[2:])  # slicing
print(courses[:3])

# add items
courses.append("Art")  # to the end
print(courses)
courses.insert(0, "Music")
print(courses)

# this adds the list as inside the other list
courses_2 = ["Literature", "Education"]
courses.insert(0, courses_2)
print(courses)
courses = []  # reset

# correct way of doing the above
courses.extend(default_courses)
print(courses)
courses.extend(courses_2)
print(courses)

# remove items
courses.remove("Math")
print(courses)
# remove the last item.. usefule for Stack DS
courses.pop()  # stack or queue
print(courses)

# reverse
courses.reverse()
print(courses)
# sorting.. alphabetically
courses.sort()
num = [1, 4, 7, 2, 0]
# sorted incrementally
num.sort()
print(courses)
print(num)

# sort in descending
courses.sort(reverse=True)
num = [1, 4, 7, 2, 0]
num.sort(reverse=True)

# sorted version of list without altering the original
courses = []
courses.extend(default_courses)
courses.extend(courses_2)
sorted_courses = sorted(courses)  # sorts in place without altering the original
print(sorted_courses)
print(courses)


# min, max, sum
print(min(num))
print(max(num))
print(sum(num))


##################
# finding values in a list
print(courses.index("CompSci"))

# check if subject is is in our list, it returns boolean
print("Art" in courses)  # False
print("Math" in courses)  # True

# Loop through items in List
for course in courses:
    print(course + "!")

# access the index and function
for index, course in enumerate(courses):
    print(index, course)
# if we need to start from a specific index
for index, course in enumerate(courses, start=1):
    print(index, course)

# we want to convert list to CSV
course_str = ", ".join(courses)
print(course_str)

# reverse the CSV to a list
new_list = course_str.split(", ")
print(new_list)
