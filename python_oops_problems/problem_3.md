# 📚 Python OOP Final Challenge – Library Management System

## 🎯 Objective

Build a **Library Management System** using Python's Object-Oriented Programming concepts.

The goal of this project is to help you master:

* Classes and Objects
* Instance Variables
* Class Variables
* Instance Methods
* Class Methods
* Static Methods
* Inheritance
* Method Overriding
* Composition
* Dunder Methods (`__str__`, `__repr__`, `__len__`)
* `super()`

---

# Requirements

## 1. Person Class

Create a base class called `Person`.

### Attributes

* `name`

---

## 2. Member Class

The `Member` class should inherit from `Person`.

### Attributes

* `member_id`
* `borrowed_books`

### Methods

#### `borrow_book(book)`

Rules:

* A member can borrow a maximum of **3 books**.
* Cannot borrow a book that is unavailable.

---

#### `return_book(book)`

Rules:

* The book should be removed from the borrowed list.
* The book should become available again.

---

## 3. Librarian Class

The `Librarian` class should inherit from `Person`.

### Methods

#### `add_book(book, library)`

Adds a book to the library.

---

#### `remove_book(book, library)`

Removes a book from the library.

---

#### `view_all_books(library)`

Displays all books in the library.

---

## 4. Book Class

### Attributes

* `title`
* `author`
* `isbn`
* `is_available`

### Class Variables

```python
total_books = 0
book_counter = 1000
```

Increment `total_books` whenever a new book is created.

---

### Methods

#### `borrow()`

Marks the book as unavailable.

---

#### `return_book()`

Marks the book as available.

---

### Dunder Methods

#### `__str__()`

Display a user-friendly representation.

Example:

```text
Title      : Atomic Habits
Author     : James Clear
ISBN       : 12345
Available  : Yes
```

---

#### `__repr__()`

Return a developer-friendly representation.

Example:

```python
Book('Atomic Habits', 'James Clear', '12345')
```

---

### Class Method

#### `generate_book(title, author, isbn)`

Automatically generate a unique book ID.

Example:

```python
book = Book.generate_book(...)
```

---

### Static Method

#### `validate_isbn(isbn)`

Return:

* `True` → if ISBN is valid
* `False` → otherwise

---

## 5. Library Class

### Attributes

* `books`
* `members`

---

### Methods

#### `register_member(member)`

Adds a member to the library.

---

#### `find_book_by_title(title)`

Returns the matching book.

---

#### `display_available_books()`

Displays only the books that are currently available.

---

#### `display_all_members()`

Displays all registered members.

---

## 6. Dunder Methods

### Member

Implement:

```python
__len__()
```

Example:

```python
len(member)
```

Should return:

```text
Number of books currently borrowed by the member.
```

---

## Bonus Features (Optional)

### Fine Calculation

A fine of **₹10 per day** should be charged for overdue books.

Use:

```python
datetime
```

to track issue dates.

---

### Transaction History

Track all actions performed in the system.

Example:

```text
Krishna borrowed "Atomic Habits"

Krishna returned "Atomic Habits"

Janvi borrowed "Deep Work"
```

---

### Export Reports

Generate reports showing:

* Available Books
* Borrowed Books
* Registered Members

---

# Example Usage

```python
library = Library()

librarian = Librarian("Alice")

member1 = Member(1, "Krishna")
member2 = Member(2, "Janvi")

library.register_member(member1)
library.register_member(member2)

book1 = Book.generate_book("Atomic Habits", "James Clear", "12345")
book2 = Book.generate_book("Deep Work", "Cal Newport", "67890")

librarian.add_book(book1, library)
librarian.add_book(book2, library)

member1.borrow_book(book1)

print(member1)

print(len(member1))

member1.return_book(book1)

library.display_available_books()
```

---

# Self-Evaluation Checklist

Mark each item once completed.

* [ ] Created all required classes
* [ ] Used inheritance correctly
* [ ] Used `super()`
* [ ] Implemented class variables
* [ ] Implemented instance variables
* [ ] Implemented instance methods
* [ ] Implemented class methods
* [ ] Implemented static methods
* [ ] Implemented `__str__`
* [ ] Implemented `__repr__`
* [ ] Implemented `__len__`
* [ ] Applied composition where appropriate
* [ ] Successfully ran the example usage without errors

---

# Challenge Rules

1. Do **not** refer to tutorials while solving.
2. Use Google only for syntax-related issues.
3. Focus on designing the classes before writing code.
4. Complete the mandatory requirements first, then attempt the bonus features.

---

## 🏆 Completion Criteria

If you can build this project from scratch and explain **why** you designed it the way you did, you can confidently say:

> "I understand Python OOP fundamentals and can model real-world systems using object-oriented design."
