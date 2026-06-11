class Employee:
    nums_of_emps = 0 
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.nums_of_emps += 1
      
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Employee.set_raise_amt(1.05)

# print(Employee.raise_amount)
# emp_1.set_raise_amt(1.06)
# print(emp_1.raise_amount)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')

# # new_emp_1 = Employee(first, last, pay)
# new_emp_1 = Employee.from_string(emp_str_1)
# new_emp_2 = Employee.from_string(emp_str_2)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# print(new_emp_2.email)
# print(new_emp_2.pay)
# print(new_emp_2.__dict__)

# Regular method takes the instance as the first argument, which is usually named self.
# Class method takes the class as the first argument, which is usually named cls.
# Static method does not take any implicit first argument, it is just like a regular function that happens to be defined inside a class.

import datetime
my_date = datetime.date(2026, 6, 11)

print(Employee.is_workday(my_date))
