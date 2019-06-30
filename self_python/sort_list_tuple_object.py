# Sorting Lists, Tuples, and Objects

# List >>>>
li = [9, 4, 1, 6, 8, 5, 3, 2, 10]
s_li = sorted(li, reverse=True)  # or li.sort(): this is sort(inplace = True)
print(s_li)
# sorted() is more flexible than .sort() since it works with tuples, lists and dict

# Tuple >>>>>
tup = (9, 4, 1, 6, 8, 5, 3, 2, 10)
s_tup = sorted(tup)
print(s_tup)
print(tuple(s_tup))

# Dictionary: >>>>>
di = {"name": "Hieu Nguyen", "job": "Data Scientist", "os": "Mac"}
s_di_val = sorted(di.values())
print(s_di_val)  # sorted by keys by default: sorted(di)

# sorted(key = arg) : extremely useful when we deal with object with name attributes
li = [-10, -7, -13, 1, 3, 4, 7, 2]
s_li = sorted(li, key=abs)  # absolute
print(s_li)


class Employee():

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return "({}, {}, $ {})".format(self.name, self.age, self.salary)


def e_sort_name(emp):
    return emp.name


def e_sort_age(emp):
    return emp.age


e1 = Employee("Hieu1", 25, 90000)
e2 = Employee("Hieu2", 35, 900000)
e3 = Employee("Hieu3", 45, 9000000)
print(e1)

e = [e1, e2, e3]
# sorted(e) will NOT work
print(sorted(e, key=e_sort_name))
print(sorted(e, key=e_sort_age, reverse=True))
# print(dir(sorted))
# USE LAMBDA
print(sorted(e, key=lambda x: x.salary))

# Use operator
# from operator import attregetter
# print(sorted(e, key= attregetter("age")))
