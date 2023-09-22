# Sets: unordered collection of values with no duplicates
# Tuples: are immutable
# Lists are mutable

list_1 = ["History", "Math", "Pysics", "CompSci"]
list_2 = list_1

print(list_1)
print(list_2)
# above is the same
list_1[0] = "Art"
print(list_1)
print(list_2)  # they both change - they are one and thesame

# Tuples ()
tuple_1 = ("History", "Math", "Pysics", "CompSci")
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = "Art"
# print(tuple_1)
# print(tuple_2)  # Error -> Immutable


######################################
# Sets {}

course_cs = {
    "History",
    "Math",
    "Pysics",
    "CompSci",
}

print(course_cs)  # produce defferent results on every rin
# sets are important because
# used to test if a value is part of a set
# use tp remove duplicates

course_cs = {"History", "Math", "Pysics", "CompSci", "Math"}  # duplicate thrown away

# sets membership test. and they are effecient
print("Math" in course_cs)


art_courses = {"History", "Math", "DrawingDesign"}  # duplicate thrown away

# check the two sets to find commonalities
print(course_cs.intersection(art_courses))

# courses in cs courses and not in art courses
print(course_cs.difference(art_courses))

# print both with all courses from sets
print(course_cs.union(art_courses))

### snippets
# Empty List
empty_list = []
empty_list = list()

# Empty Tuples
empty_list = ()
empty_list = tuple()

# Empty List
empty_list = {}  # this isn't right , its a dict
empty_list = set()
