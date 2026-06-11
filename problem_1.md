# 🐍 Python OOP Challenge – Employee Management System

## Objective

Build an **Employee Management System** using Object-Oriented Programming concepts in Python. This challenge is designed to test your understanding of all the major topics covered in Corey Schafer's OOP playlist.

---

## Requirements

### 1. Employee Class

Create a class named `Employee`.

#### Instance Attributes

* `first`
* `last`
* `pay`

#### Class Attributes

* `raise_amount = 1.04`
* `num_of_employees = 0`

---

### 2. Instance Methods

Implement the following methods:

#### `fullname()`

Returns the employee's full name.

**Example:**

```python
emp.fullname()
# Output: John Doe
```

#### `apply_raise()`

Updates the employee's salary using `raise_amount`.

---

### 3. Class Methods

Implement the following class methods:

#### `set_raise_amt(amount)`

Updates the raise amount for all employees.

#### `from_string(emp_str)`

Creates an `Employee` object from a string.

**Example:**

```python
emp = Employee.from_string("John-Doe-50000")
```

---

### 4. Static Method

Implement:

#### `is_workday(date)`

Returns `True` if the given date is a weekday and `False` otherwise.

---

### 5. Special (Dunder) Methods

Implement the following:

#### `__repr__`

Returns an unambiguous representation of the object.

#### `__str__`

Returns a user-friendly representation of the object.

#### `__add__`

Adding two employees should return the sum of their salaries.

**Example:**

```python
emp1 + emp2
# Output: 110000
```

#### `__len__`

Returns the number of characters in the employee's full name.

---

### 6. Developer Class

Create a subclass named `Developer`.

#### Additional Attribute

* `prog_lang`

#### Modified Class Attribute

```python
raise_amount = 1.10
```

---

### 7. Manager Class

Create a subclass named `Manager`.

#### Additional Attribute

* A list of employees managed by the manager.

#### Methods

* `add_emp(emp)`
* `remove_emp(emp)`
* `print_emps()`

---

### 8. Properties

Convert the following into properties:

#### `email`

Access it without parentheses.

**Example:**

```python
emp.email
```

---

#### `fullname`

Implement:

* `@property`
* `@fullname.setter`
* `@fullname.deleter`

**Setter Example:**

```python
emp.fullname = "Jane Smith"
```

**Deleter Example:**

```python
del emp.fullname
```

After deletion:

* Print `"Delete Name!"`
* Set `first` and `last` to `None`

---

## Final Verification

Your implementation should successfully execute the following code:

```python
dev1 = Developer("Krishna", "Prasath", 70000, "Python")
dev2 = Developer.from_string("John-Doe-80000")

mgr = Manager("Alice", "Boss", 100000, [dev1])

mgr.add_emp(dev2)
mgr.print_emps()

print(dev1.email)
print(dev1.fullname)

print(dev1 + dev2)
print(len(dev1))

dev1.fullname = "Corey Schafer"
print(dev1.email)

del dev1.fullname
```

---

## Self-Evaluation Checklist

Mark each item once you complete it.

* [ ] Created the `Employee` class
* [ ] Used class variables correctly
* [ ] Implemented instance methods
* [ ] Implemented class methods
* [ ] Implemented a static method
* [ ] Used inheritance effectively
* [ ] Used `super()`
* [ ] Implemented dunder methods
* [ ] Implemented properties, setters, and deleters
* [ ] Successfully ran the final verification code without errors

---

## Challenge Rule

> **Do not refer back to Corey Schafer's code while solving this problem.**
>
> If you can complete this challenge from memory and explain every line you wrote, you have a solid understanding of Python OOP fundamentals.
