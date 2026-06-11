class Employee:
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
      
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 
    
    
class Developer(Employee):  
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay) # this will call the __init__ method from the Employee class, which will initialize the first, last, email and pay attributes.
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay) # this will call the __init__ method from the Employee class, which will initialize the first, last, email and pay attributes.
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')
mgr_1 = Manager('John', 'Doe', 80000, [dev_1, dev_2])


print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee)) # True, since Developer is a subclass of Employee
print(issubclass(Manager, Developer)) # False, since Manager is not a subclass of Developer

# print(dev_1.pay) # this will show the method resolution order (MRO) of the class Developer, which is Developer -> Employee -> object.
# dev_1.apply_raise() # this will call the apply_raise method from the Employee class, since it is not defined in the Developer class.
# print(dev_1.pay)

# print(dev_1.prog_lang)

# mgr_1.add_emp(dev_1)
# mgr_1.remove_emp(dev_2)

# print(mgr_1.email)
# mgr_1.print_emps()


# Avoid using mutable objects like lists ([], dictionaries {}, or sets set())
# as default argument values.
#
# If you use a list as a default value, that same list is shared across
# all instances of the class, which can lead to unexpected behavior.
#
# Instead, use None as the default value and create a new list inside
# the constructor. This ensures that each object gets its own separate list.

#----------------------------------------------------------------------------------

# Help on class Developer in module __main__:                                                                                                                    

# class Developer(Employee)
#  |  Developer(first, last, pay)
#  |
#  |  Method resolution order:
#  |      Developer
#  |      Employee
#  |      builtins.object
#  |
#  |  Methods inherited from Employee:
#  |
#  |  __init__(self, first, last, pay)
#  |      Initialize self.  See help(type(self)) for accurate signature.                                                                                         
#  |                                                                                                                                                             
#  |  apply_raise(self)                                                                                                                                          
#  |                                                                                                                                                             
#  |  fullname(self)                                                                                                                                             
#  |                                                                                                                                                             
#  |  ----------------------------------------------------------------------                                                                                     
#  |  Data descriptors inherited from Employee:                                                                                                                  
#  |                                                                                                                                                             
#  |  __dict__                                                                                                                                                   
#  |      dictionary for instance variables                                                                                                                      
#  |                                                                                                                                                             
#  |  __weakref__                                                                                                                                                
#  |      list of weak references to the object                                                                                                                  
#  |                                                                                                                                                             
#  |  ----------------------------------------------------------------------                                                                                     
#  |  Data and other attributes inherited from Employee:                                                                                                         
#  |                                                                                                                                                             
#  |  raise_amount = 1.04                                                                                                                                        

# None
# Corey.Schafer@company.com
# Test.User@company.com