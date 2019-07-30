## SPECIAL (MAGIC/DUNER) METHODS ##
"""
Dunder means double underscore: dunder init <=> __init__

https://docs.python.org/3/reference/datamodel.html#special-method-names
"""


class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.last = last
        self.first = first
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def __repr__(self):  # this is used to show object's info to developer
        # used for logging & debugging purposes
        # useful to recreate an onject creation --> ez to copy and paste
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        # this is used to show info to the end users since it is more readable
        return "{} - {}".format(self.fullname(), self.email)

    # Addition of employees' salaries
    def __add__(self, other):
        return self.pay + other.pay

    # return total of characters in employees fullname
    def __len__(self):
        return len(self.fullname())


emp1 = Employee("Hieu", "Nguyen", 150000)
emp2 = Employee("Hoa", "Nguyen", 100000)

print(emp1)  # __str__ is used to print emp1 by DEFAULT: Hieu Nguyen - Hieu.Nguyen@gmail.com
print(repr(emp1))  # Employee(Hieu, Nguyen, 150000)

print(int.__add__(1, 2))  # <=> 1 + 2 = 3
print(emp1 + emp2)  # <=> 250000 = 150000 + 100000
