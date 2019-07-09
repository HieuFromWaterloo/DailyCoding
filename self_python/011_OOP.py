# 1. Class and Instances >>>>>>>>>>>>>>>>>>

"""
In the back ground when we call: emp1.fullname()
---> print(Employee.fullname(emp1))
"""

# 2. Class variable >>>>>>>>>>>>>
"""
we can ezly overwrite raise_amount instances with different employees
    - we can set emp1.raise_amount = 1.05
    - we can set emp2.raise_amount = 1.02
    - And the rest of self.raise_amount = 1.04 as Employee.raise_amount
"""


class Employee:
    raise_amount = 1.04  # Class variable: 4% raise
    num_emp = 0 # Class var to keep track of how many emp

    def __init__(self, first, last, pay):    # these are instances
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@hyperdata.ca"

        # since init runs everytime we create a new emp
        Employee.num_emp += 1
        # DO NOT use self.num_emp because this cannot be affected by any other instances within a class
        # and we will not be using this variable anywhere else below

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        # Using Class Variable - raise_amount
        self.pay = int(self.pay * self.raise_amount)  # OR
        # self.pay = int(self.pay * Employee.raise_amount)
        # DO NOT HARDCODED HERE: self.pay = int(self.pay * 1.04)


emp1 = Employee("hieu", "nguyen", 1000000)
emp2 = Employee("hoa", "nguyen", 2000000)

print(emp1.__dict__)  # {'pay': 1000000, 'last': 'nguyen', 'email': 'hieu.nguyen@hyperdata.ca', 'first': 'hieu'}

# Employee.raise_amount = 1.05 # This will change the entire class var value
print(Employee.__dict__)
# {'__module__': '__main__', '__init__': <function __init__ at 0x105ee6050>, 'raise_amount': 1.04, 'fullname': <function fullname at 0x105ee6668>, '__doc__': None, 'apply_raise': <function apply_raise at 0x105ee6d70>}
