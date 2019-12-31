# List, tuples, sets

##########################################
# List >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
##########################################

# empty list:
emp_list = []  # or list()

courses = ["History", "Math", "CS", "Stat"]
courses_2 = ["SCI", "COMM"]

# alst.append: add 1 element to the end of the
courses.append("CO")

# alst.insert(index, what_to_insert): allows insert element into a specific index
courses.insert(0, "ECON")  # insert in the beginning of the list

# add 2+ elements: alst.extend(alist_of_items) to the end of the list
courses.extend(courses_2)
# NOTE if we use courses.insert(0, course_2) we will get:
# [["SCI", "COMM"], "History", "Math", "CS", "Stat"]

# alst.remove(an_item_in_alst)
courses.remove("Math")

# alst.pop(): by default remove the last item in the list, AND returns the value being removed
# useful if we wanna use our list a stack or a queue
var_removed = courses.pop()  # "stat"

# Reverse
courses.reverse()

# Sort: default - alphabetically and ascending order, IN PLACE
courses.sort()
courses.sort(reverse=True)  # descending order

# Sort WITHOUT Inplace: return the sorted version of the original list
sorted_list = sorted(courses)

# .min(), .max(), .sum(), .mean()

# Search for index of elements in a list
print(courses)  # ['Stat', 'SCI', 'History', 'ECON', 'CS', 'CO']
print(courses.index("CS"))  # return 4

# Enumerate:
for index, item in enumerate(courses, start=1):  # by default it starts at 0
    print(index, item)

# join strings:
courses_str = ", ".join(courses)
print(courses_str)  # Stat, SCI, History, ECON, CS, CO
# string to list just: str.split(", ")

# list is MUTABLE:
courses_3 = courses  # = ['Stat', 'SCI', 'History', 'ECON', 'CS', 'CO']

# now if we set an element of courses in to sth else, course_3 WILL BE MUTATED accordingly
courses[0] = "Art"  # change "Stat" to "Art"
print(courses)  # ['Art', 'SCI', 'History', 'ECON', 'CS', 'CO']
print(courses_3)  # ['Art', 'SCI', 'History', 'ECON', 'CS', 'CO']: also be mutated
# this is because they're both mutable objects
# to getover this we need tuple


##########################################
# Tuple >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
##########################################

"""
Tuple is very similar to list except we cannot modify tuple (NOT MUTABLE)
"""

# empty tuple
emp_tuple = ()  # or tuple()

tuple_1 = ('Stat', 'SCI', 'History', 'ECON', 'CS', 'CO')
tuple_2 = tuple_1

# TypeError: 'tuple' object does not support item assignment
# tuple_1[0] = "Art"  # this is because tuple is IMMUTABLE
# this why tuple does not have as many methods as a list

##########################################
# Set: unordered, no duplicate >>>>>>>>>>>
##########################################

"""
- membership test is a lot more efficient with set
- also use for difference, intersection, union
"""

# empty set
emp_set = {} # or set()
