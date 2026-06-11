#Class variable are variables that are shared among all instances of a class. 
#Instance variables are variables that are unique to each instance of a class.

class Employee:
    nums_of_emps = 0 
    raise_amount = 1.05 # this is a class variable, it is shared among all instances of the class Employee.
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
    #we need to access it using the class name Employee.raise_amount or self.raise_amount
    #NameError: name 'raise_amount' is not defined. Did you mean: 'self.raise_amount'?

print(Employee.nums_of_emps) # 0 -> Before creating any instance of the class Employee, the class variable nums_of_emps is 0.

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
#print(Employee.__dict__) # this will print the instance variables of emp_1

# Employee.raise_amount = 1.06 # we can change the class variable using the class name, but it will not change the class variable for the instances that have already been created. 
# emp_1.raise_amount = 1.07 # we can change the class variable for a specific instance, but it will not change the class variable for the other instances.

# print(emp_1.__dict__)
# print(Employee.raise_amount) 
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(Employee.raise_amount) # we can access the class variable using the class name.
# print(emp_1.raise_amount) # we can access the class variable using the instance, but it is not recommended.
# print(emp_2.raise_amount)

print(Employee.nums_of_emps) # we can access the class variable using the class name.