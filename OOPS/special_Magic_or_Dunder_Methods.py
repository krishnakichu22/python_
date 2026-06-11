class Employee:
    raise_amount = 1.05

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

# Special methods (also called dunder methods, since they have double underscores before and after the method name)
#  are special methods that are used to define the behavior of an object when it is used in a certain way. 
# For example, the __init__ method is called when an object is created,
#  and the __str__ method is called when an object is printed.

# The __repr__ method is used to define the string representation of an object, which is used for debugging and logging purposes.
# The __str__ method is used to define the string representation of an object, which is used for user-friendly display purposes.

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1 + emp_2)

print(len(emp_1))
print(len(emp_2))

# print(emp_1) # this will call the __str__ method, since it is defined in the Employee class.
# print(repr(emp_1)) # this will call the __repr__ method, since it is defined in the Employee class.
# print(str(emp_1)) # this will call the __str__ method, since it is defined in the Employee class.

# If str is not defined, then the __repr__ method will be used as a fallback for the string representation of the object.
# If str is defined, then the __repr__ method will be used as a fallback 
# for the string representation of the object when the object is printed in a list or a dictionary.

#print(emp_1.__repr__()) # this will call the __repr__ method, since it is defined in the Employee class.
#print(emp_1.__str__()) # this will call the __str__ method, since it is defined in the Employee class.


## More Dunder Methods

#print(int.__add__(2,3)) # this will call the __add__ method of the int class, which will return the sum of 2 and 3, which is 5.
#print(str.__add__('Hello', 'World')) # this will call the __add__ method of the str class, which will return the concatenation of 'Hello' and 'World', which is 'HelloWorld'.

print(len('test')) # this will call the __len__ method of the str class, which will return the length of the string 'test', which is 4.
print('test'.__len__()) # this will call the __len__ method of the str class, which will return the length of the string 'test', which is 4.
