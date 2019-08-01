# Property Decorator: Getters, Setters, Deleters

"""
The property decorator "@property" allows us to define a method where we can access it like an attribute

ex: say if we want the email to be updated whenever there are changes in first or last name
"""


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com"

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # Setter
    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        print((first, last))
        self.first = first
        self.last = last
        # now we can do emp1.fullname("Dung Nguyen")

    # Deleter
    @fullname.deleter
    def fullname(self):
        print("Deleter Activated")
        self.first = None
        self.last = None
        # use del to execute


emp1 = Employee("Hieu", "Nguyen")
# NOTE ## fullname() is a method but here we can access it as if it is an attribute
# there is no need to call: emp1.fullname()
print(emp1.fullname)

emp1.first = "Hoa"
print(emp1.fullname)  # the fullname is automatically updated accordingly

# --- If we wanna update the entire fullname: use Setter
emp1.fullname = "Dung Nguyen"
print(emp1.first)
print(emp1.fullname)

del emp1.fullname
