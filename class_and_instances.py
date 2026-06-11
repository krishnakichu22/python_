# Python Object Oriented Programming


class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
      
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    #TypeError: Employee.fullname() takes 0 positional arguments but 1 was given if we miss the self at the method fullname()

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.fullname())
print(emp_2.fullname())
#emp2 is automatically passed as the first argument to the method fullname() and it is assigned to self, so we can access the attributes of emp_2 using self in the method fullname().
print(Employee.fullname(emp_1)) # we can also call the method like this by passing the object as an argument, but it is not recommended.

#print('{} {}'.format(emp_1.first,emp_1.last)) # instead of doing like this we can add this into the class as a method and call it like.

# Which prints the memory location of the objects, which is different for each object
# <__main__.Employee object at 0x00000259B9AD6690>
# <__main__.Employee object at 0x00000259B9AD6600>

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'corey.schafer@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)  

# corey.schafer@company.com
# Test.User@company.com