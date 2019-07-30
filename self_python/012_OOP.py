# Inheritance - Create Subclass


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

# Create a sub class with inheritance


class Developer(Employee):
    # just simply do "pass", this class automatically inherit all the methods from the super class
    raise_amt = 1.10  # we can have customize rate
    # Add a programming language

    def __init__(self, first, last, pay, pro_lang):
        # Let the super class handle the first, last, and pay
        # super().__init__(first, last, pay)  # OR
        Employee.__init__(self, first, last, pay)
        # using super is simpler to maintain
        self.pro_lang = pro_lang


class Manager(Employee):
    raise_amt = 1.2

    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        # It is not a good practice to pass in iterable object like list as a default param
        if employees is None:  # NOTE #####
            self.employees = []
        else:
            self.employees = employees

    # Add employee
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # Remove employee
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # print emp
    def print_emp(self):
        for emp in self.employees:
            print("--->", emp.fullname())  # DO NOT FORGET THE () because fullname is a method


emp1 = Developer("hieu", "nguyen", 1000000, "python")
emp2 = Developer("hoa", "nguyen", 2000000, "python")

# print(help(Developer))
# print(emp1.email)

mger1 = Manager("Hien", "Nguyen", 300000, [emp1])
print(mger1.email)
print(mger1.print_emp())

##### CHECK IF an object is inheritance instance of a class ####
print(isinstance(mger1, Manager))  # True
print(isinstance(mger1, Employee))  # True
print(isinstance(emp1, Manager))  # False: emp does not inherit from Manager

# CHECK IF subclass: ####3
print(issubclass(Employee, Manager))  # false
print(issubclass(Manager, Employee))  # True
print(issubclass(Developer, Manager))  # False
