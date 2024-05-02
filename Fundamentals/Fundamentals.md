# Python Fundamentals: Basics of Programming

## What are variables in Python?
Variables in Python are used to store and manipulate data. They act as named containers for values. In Python, variables do not need to be explicitly declared with a type, and their type can change dynamically based on the value assigned to them. Variable names must follow certain rules:
- Must start with a letter or underscore (_)
- Can only contain letters, numbers, and underscores
- Case-sensitive

Example:
```python
# Variable assignment
x = 10
name = "Alice"
is_active = True

# Variable reassignment
x = 20
```

## What are data types in Python?
Python supports various data types, including:
- Integer (`int`): whole numbers without decimal points
- Float (`float`): numbers with decimal points
- String (`str`): sequence of characters enclosed in quotes
- Boolean (`bool`): represents True or False
- List (`list`): ordered collection of items
- Tuple (`tuple`): ordered, immutable collection of items
- Dictionary (`dict`): unordered collection of key-value pairs

Example:
```python
# Integer
age = 25

# Float
height = 5.9

# String
name = "Alice"

# Boolean
is_active = True

# List
numbers = [1, 2, 3]

# Tuple
coordinates = (10, 20)

# Dictionary
person = {"name": "Bob", "age": 30}
```

## How do you perform arithmetic operations in Python?
Python supports various arithmetic operations, including addition (+), subtraction (-), multiplication (*), division (/), modulus (%), and exponentiation (**).

Example:
```python
x = 10
y = 5

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
modulus = x % y
exponentiation = x ** y
```

## What are comments in Python?
Comments in Python are used to add explanations or notes within the code. They are ignored by the Python interpreter during execution. Comments start with the `#` symbol and can be placed on a separate line or at the end of a line of code.

Example:
```python
# This is a single-line comment

print("Hello, World!")  # This is also a comment
```

## How do you use conditional statements in Python?
Conditional statements, such as `if`, `elif`, and `else`, are used for decision-making in Python. They allow the program to execute different blocks of code based on specified conditions.

Example:
```python
x = 10

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

---

This Readme file covers the basics of programming in Python, including variables, data types, arithmetic operations, comments, and conditional statements. Each concept is explained concisely with examples for better understanding.