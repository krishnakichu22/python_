# 🏦 Python OOP Challenge – Banking System

## Objective

Design and implement a simple Banking System using Object-Oriented Programming principles in Python.

---

## Requirements

### 1. Create an `Account` class

#### Instance Attributes

* `account_number`
* `holder_name`
* `balance`

#### Class Attributes

* `bank_name = "Python National Bank"`
* `total_accounts = 0`

---

### 2. Implement the following methods

#### `deposit(amount)`

* Add money to the account.
* Print the updated balance.

---

#### `withdraw(amount)`

* Deduct money from the account.
* Prevent withdrawals if the balance is insufficient.

---

#### `check_balance()`

* Display the current account balance.

---

#### `transfer(other_account, amount)`

* Transfer money from one account to another.
* Ensure sufficient balance before transferring.

---

### 3. Implement Dunder Methods

#### `__str__`

Return a user-friendly representation.

**Example:**

```text
Account Holder: John Doe
Account Number: 12345
Balance: ₹50,000
```

---

#### `__repr__`

Return an unambiguous representation of the object.

---

### 4. Savings Account

Create a subclass called `SavingsAccount`.

#### Additional Attribute

* `interest_rate`

#### Method

##### `apply_interest()`

* Increase the balance according to the interest rate.

---

### 5. Current Account

Create a subclass called `CurrentAccount`.

#### Additional Attribute

* `overdraft_limit`

#### Requirement

Allow withdrawals beyond the balance up to the overdraft limit.

---

### 6. Class Methods

Implement:

#### `change_bank_name(new_name)`

* Update the bank name for all accounts.

---

### 7. Static Method

Implement:

#### `validate_amount(amount)`

Returns:

* `True` if the amount is positive.
* `False` otherwise.

Use this method inside `deposit()` and `withdraw()`.

---

## Sample Usage

Your implementation should support the following:

```python
acc1 = SavingsAccount(1001, "Krishna", 50000, 5)
acc2 = CurrentAccount(1002, "Rahul", 10000, 20000)

acc1.deposit(5000)
acc1.withdraw(2000)

acc1.transfer(acc2, 10000)

acc1.apply_interest()

acc2.withdraw(25000)

print(acc1)
print(acc2)
```

---

## Bonus Features (Optional)

* [ ] Maintain a transaction history list.
* [ ] Implement a method to print the transaction history.
* [ ] Generate account numbers automatically.
* [ ] Prevent duplicate account numbers.

---

## Self-Assessment

If you can solve this without looking up examples, you are comfortable with:

* [ ] Classes and Objects
* [ ] Class Variables
* [ ] Instance Variables
* [ ] Instance Methods
* [ ] Class Methods
* [ ] Static Methods
* [ ] Inheritance
* [ ] Method Overriding
* [ ] Dunder Methods
* [ ] Using OOP to model real-world systems

---

### Challenge Rule

> Focus on designing the classes yourself before writing code.
>
> Ask yourself:
>
> * Which behavior belongs to the parent class?
> * What should the child classes override?
> * How can code duplication be minimized?
