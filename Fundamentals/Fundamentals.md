## Python Fundamentals

---

## What are variables in Python?
Variables in Python are used to store and manipulate data. They act as named containers for values. In Python, variables do not need to be explicitly declared with a type, and their type can change dynamically based on the value assigned to them. Variable names must follow certain rules:
- Must start with a letter or underscore (_)
- Can only contain letters, numbers, and underscores
- Case-sensitive

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

```python
# This is a single-line comment

print("Hello, World!")  # This is also a comment
```

## How do you use conditional statements in Python?
Conditional statements, such as `if`, `elif`, and `else`, are used for decision-making in Python. They allow the program to execute different blocks of code based on specified conditions.

```python
x = 10

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

## How do you use loops in Python?
Loops in Python are used to execute a block of code repeatedly. Python supports two main types of loops: `for` loops and `while` loops.

- **For Loop:** Iterates over a sequence (e.g., list, tuple, string) or any iterable object.
  ```python
  # Example of a for loop
  numbers = [1, 2, 3, 4, 5]

  for num in numbers:
      print(num)
  ```
- **While Loop:** Executes a block of code as long as a specified condition is true.
  ```python
  # Example of a while loop
  count = 0

  while count < 5:
      print(count)
      count += 1
  ```

## What are functions in Python?
Functions in Python are reusable blocks of code that perform a specific task. They allow you to break down your program into smaller, manageable pieces, making your code more organized and easier to maintain.

## How do you define and call functions in Python?
To define a function in Python, you use the `def` keyword followed by the function name and parameters (if any). The function body contains the code to be executed when the function is called.

```python
# Example of defining a function
def greet(name):
    print("Hello, " + name + "!")
```
To call a function in Python, simply use the function name followed by parentheses and provide any required arguments.
```python
# Example of calling a function
greet("Alice")
```

## What are parameters and arguments in Python functions?
- **Parameters:** Parameters are variables listed inside the parentheses of a function definition. They are used to pass information into a function.
- **Arguments:** Arguments are the actual values passed to a function when it is called. They match the parameters defined in the function header.

Example:
```python
# Function definition with a parameter
def greet(name):
    print("Hello, " + name + "!")
    
# Function call with an argument
greet("Bob")
```

## What is the return statement in Python?
The `return` statement in Python is used to exit a function and return a value to the caller. It can be used to pass data back from the function to the calling code.
```python
# Example of a function with a return statement
def add(x, y):
    return x + y

result = add(3, 5)
print(result)  # Output: 8
```

## How do you handle user input in Python?
In Python, you can use the `input()` function to prompt the user for input. The `input()` function reads a line from the user's input and returns it as a string.
```python
# Example of handling user input
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

## What are strings in Python?
Strings in Python are sequences of characters, enclosed in single (' '), double (" "), or triple (''' ''' or """ """) quotes. They can contain letters, numbers, symbols, and whitespace.
```python
# Example of strings
name = "Alice"
message = 'Hello, World!'
multiline = '''This is a 
multiline string.'''
```

## How do you format strings in Python?
Python provides various ways to format strings:
- **Using the `format()` method:** Insert variables into strings by specifying placeholders (`{}`) and passing values to the `format()` method.
  ```python
  # Example of string formatting
  name = "Alice"
  age = 30
  message = "My name is {} and I am {} years old.".format(name, age)
  ```
- **Using f-strings (formatted string literals):** Prefix a string with `f` or `F` and embed expressions within curly braces `{}`.
  ```python
  # Example of f-strings
  name = "Alice"
  age = 30
  message = f"My name is {name} and I am {age} years old."
  ```

## What are lists in Python?
Lists in Python are ordered collections of items, which can be of different data types. They are mutable, meaning their elements can be changed after creation. Lists are defined using square brackets `[]`.
```python
# Example of lists
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']
mixed = [1, 'hello', True]
```

## How do you access and manipulate elements in lists?
You can access elements in a list using index notation (`[]`). Lists in Python are zero-indexed, meaning the first element has an index of 0.
```python
# Example of accessing list elements
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # Output: 1
print(numbers[-1])  # Output: 5 (negative index counts from the end)

# Example of manipulating list elements
numbers[0] = 10  # Modify the first element
numbers.append(6)  # Add an element to the end of the list
numbers.remove(2)  # Remove an element by value
```

## What are tuples in Python?
Tuples in Python are ordered collections of items, similar to lists, but they are immutable, meaning their elements cannot be changed after creation. Tuples are defined using parentheses `()`.
```python
# Example of tuples
coordinates = (10, 20)
colors = ('red', 'green', 'blue')
```

## What are dictionaries in Python?
Dictionaries in Python are unordered collections of key-value pairs. They are used to store data in a structured format, where each value is associated with a unique key. Dictionaries are defined using curly braces `{}` and key-value pairs separated by colons `:`.

```python
# Example of dictionaries
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

## How do you work with dictionaries in Python?
You can access, add, modify, and remove elements in dictionaries using various methods and built-in functions.
```python
# Example of working with dictionaries
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing elements
print(person['name'])  # Output: Alice

# Adding elements
person['email'] = 'alice@example.com'

# Modifying elements
person['age'] = 31

# Removing elements
del person['city']
```

## What are sets in Python?
Sets in Python are unordered collections of unique elements. They are used to perform mathematical set operations such as union, intersection, difference, and symmetric difference. Sets are defined using curly braces `{}` or the `set()` constructor.

```python
# Example of sets
set1 = {1, 2, 3, 4, 5}
set2 = set([4, 5, 6, 7, 8])
```

## How do you perform set operations in Python?
Python provides various methods and operators for performing set operations.
- **Union (`|`):** Returns a set containing all unique elements from both sets.
- **Intersection (`&`):** Returns a set containing only the elements that are common to both sets.
- **Difference (`-`):** Returns a set containing the elements that are in the first set but not in the second set.
- **Symmetric Difference (`^`):** Returns a set containing the elements that are in either of the sets, but not both.

```python
# Example of set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2
symmetric_difference_set = set1 ^ set2
```

## What are boolean expressions in Python?
Boolean expressions in Python are expressions that evaluate to either True or False. They are used in conditional statements, loops, and logical operations. Python provides various boolean operators such as `and`, `or`, and `not` for combining boolean expressions.

```python
# Example of boolean expressions
x = 5
y = 10

# Comparison operators
print(x > y)  # Output: False

# Logical operators
print(x > 0 and y > 0)  # Output: True
print(x > 0 or y < 0)   # Output: True
print(not x == y)       # Output: True
```

---
