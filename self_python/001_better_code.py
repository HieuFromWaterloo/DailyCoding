dir(object)  # OR
help(object)

# Tip 1: >>>>>>>>
condition = False
x = 1 if condition else 0
print(x)

# tip 2: >>>>>>>>>>
num1 = 10_000_000_000
num2 = 10_000_000
total = num1 + num2

print(f"{total:,}")  # print format with ",": 1,000,000

# Opening and closing files: using context manager >>>>>>>>>>>>>>>>>>>>
with open("textfile.txt", "r"):
    file_contents = f.read()
    words = file_contents.split(" ")
    words_count = len(words)

print(words_count)

# Enumerate: >>>>>>>>>>>>>
alist = ["Hieu", "Morris", "Diana", "Kirtan"]
roles = ["vietnamese", "taiwanese", "irish", "indian"]
unis = ["waterloo", "toronto", "brock", "ubc"]

for index, item in enumerate(alist, start=0):  # start at 1 by default
    print(index, item)  # 0 hieu, 1 morris, ....

# Zip: >>>>>>>> Allows moving over 2+ lists at a time
for name, role, uni in zip(alist, roles, unis):
    print(f"{name} is {role} from {uni}")

for value in zip(alist, roles, unis):
    print(value)  # output will be a tuple without being unpacked

# Ignore Variable when unpacking:
a, _ = (1, 2)

# Too many values to unpack:
a, b, c = (1, 2, 3, 4, 5)  # will get errors

a, b, *c = (1, 2, 3, 4, 5)  # a=1, b=2, c = [3,4,5]

a, b, *_ = (1, 2, 3, 4, 5)  # ignore everything after 3

a, b, *c, d = (1, 2, 3, 4, 5)  # a=1,b=2, c = [3,4], d = 5

# Getting and Setting attributes to a Class: >>>>>>>>>>>>>>>>>>>>>


class Person():
    pass


person = Person()

# dynamic adding instances to class
person.first = "Hieu"
person.last = "Nguyen"

print(person.first)  # Hieu
print(person.last)  # Nguyen

# What if the values we wanna add is the ATTRIBUTES of another VAR
first_key = "first"
first_val = "Hieu"

# We cannot!:
person.first_key = first_val
# because then our attribute name will no longer be first, instead first_key

# use: setattr(object, attribute, value) && getattr()
setattr(person, first_key, first_val)
print(person.first)  # Hieu
first = getattr(person, first_key)  # Hieu

# Loop over items in Dict THEN ADD attributes to person Class >>>>>>>>>>>>>>>>>
person_info = {"first": "Hieu", "last": "Nguyen"}

for key, val in person_info.items():
    setattr(person, key, val)

print(person.first)  # Hieu
print(person.last)  # Nguyen

for key in person_info.keys():
    print(getattr(person, key))  # Hieu Nguyen

# INPUT INFO INTO SYSTEM SALTED >>>>>>>>>>>>>>>>>>>>
# Old:
username = input("username: ")
pw = input("password: ")
print("loging in...")
# getpass instead of input
from getpass import getpass
username = input("username: ")
pw = getpass("password: ")
print("loging in...")

# RUN A MODEL FROM DIFFERENT ENV/DIR: -m searching through directories,
python - m moule_name - c argument_c_required_for_module - n argument_n_required_for_module
# NOTE: module_name".py" not required
