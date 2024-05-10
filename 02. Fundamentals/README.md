# Python Fundamentals

### Variables
Variables in Python are containers used to store data. They serve as named references to objects in memory. Python is dynamically typed, meaning variables do not require explicit declaration of data types and can change types dynamically. Variable names must follow certain rules:
- Must start with a letter or underscore (_)
- Can only contain letters, numbers, and underscores
- Case-sensitive

```python
# Examples of Variables
x = 10
name = "Kante"
is_active = True

# Variable reassignment
x = 20
```

### Data Types
Python supports various data types, including:
- Integer (`int`): whole numbers without decimal points
- Float (`float`): numbers with decimal points
- String (`str`): sequence of characters enclosed in quotes
- Boolean (`bool`): represents True or False
- List (`list`): ordered collection of items
- Tuple (`tuple`): ordered, immutable collection of items
- Dictionary (`dict`): unordered collection of key-value pairs
- Set (`set`): unordered collection of unique elements

```python
# Examples of data types
age = 25 # Integer
height = 5.9 # Float
name = "Kante" # String
is_active = True # Boolean
numbers = [1, 2, 3] # List
coordinates = (10, 20) # Tuple
person = {"name": "Kante", "age": 30} # Dictionary
set1 = {1, 2, 3, 4, 5} # set
```

### Arithmetic Operations
Python supports various arithmetic operations, including addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), modulus (`%`), and exponentiation (`**`).

```python
# Examples for Arithmetic Operations
x = 10
y = 5

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
modulus = x % y
exponentiation = x ** y
```



### Comments
Comments in Python start with the `#` symbol and are used for adding explanations or notes within the code. They are ignored by the Python interpreter during execution. Comments start with the `#` symbol and can be placed on a separate line or at the end of a line of code.

```python
# Example: This is a single-line comment

print("Hello, World!")  # Example: This is also a comment
```

### Conditional Statements
Conditional statements, such as `if`, `elif`, and `else`, are used for decision-making in Python. They allow the program to execute different blocks of code based on specified conditions.

```python
# Example for a Conditional statement
x = 10

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

### Loops
Python supports `for` and `while` loops for executing a block of code repeatedly.

```python
# Example of a for loop
numbers = [1, 2, 3, 4, 5]

for num in numbers: # Iterates over a sequence (e.g., list, tuple, string) or any iterable object.
    print(num)

# Example of a while loop
count = 0

while count < 5: # Executes a block of code as long as a specified condition is true.
    print(count)
    count += 1
```

### Functions
Functions in Python are reusable blocks of code that perform specific tasks, enhancing code organization and maintainability. They are defined using the `def` keyword followed by the function name and parameters (if any).The function body contains the code to be executed when the function is called.

```python
# Example of defining a function
def greet(name):
    print("Hello, " + name + "!")
```
To call a function in Python, simply use the function name followed by parentheses and provide any required arguments.
```python
# Example of calling a function
greet("Kanté")
```

### Parameters and Arguments
Parameters are variables listed inside the parentheses of a function definition, while arguments are the actual values passed to a function when it is called. They match the parameters defined in the function header.

```python
# Function definition with a parameter name
def greet(name):
    print("Hello, " + name + "!")
    
# Function call with an argument object/value of name
greet("Bob")
```

### Return Statement
The `return` statement in Python is used to exit a function and return a value to the caller.

```python
# Example of a function with a return statement
def add(x, y):
    return x + y

result = add(3, 5)
print(result)  # Output: 8
```

### User Input
Python's `input()` function is used to prompt users for input. It reads a line from the user's input and returns it as a string.

```python
# Example of handling user input
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

### Strings
Strings in Python are sequences of characters, enclosed in single (' '), double (" "), or triple (''' ''' or """ """) quotes. They can contain letters, numbers, symbols, and whitespace.

```python
# Example of strings
name = "Kanté"
message = 'Hello, World!'
multiline = '''This is a 
multiline string.'''
```

### String Formatting
Python provides various ways to format strings, including the `format()` method and f-strings (formatted string literals).

```python
# Example of format method: Insert variable placeholders (`{}`) and pass values to the `format()` method.
name = "Alice"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)

# Example of f-strings: Prefix a string with `f` or `F` and embed expressions within curly braces `{}
message = f"My name is {name} and I am {age} years old."
```

### Lists
Lists in Python are ordered collections of items, which can be of different data types. They are mutable, meaning their elements can be changed after creation. Lists are defined using square brackets `[]`.

```python
# Example of lists
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']
mixed = [1, 'hello', True]
```

### Accessing and Manipulating List Elements
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

### Tuples
Tuples in Python are ordered collections of items, similar to lists, but they are immutable, meaning their elements cannot be changed after creation. Tuples are defined using parentheses `()`.

```python
# Example of tuples
coordinates = (10, 20)
colors = ('red', 'green', 'blue')
```

### Dictionaries
Dictionaries in Python are unordered collections of key-value pairs. They are used to store data in a structured format, where each value is associated with a unique key. Dictionaries are defined using curly braces `{}` and key-value pairs separated by colons `:`.

```python
# Example of dictionaries
person = {'name': 'Kanté', 'age': 30, 'city': 'London'}
```

### Working with Dictionaries
You can access, add, modify, and remove elements in dictionaries using various methods and built-in functions.

```python
# Example of working with dictionaries
person = {'name': 'Kanté', 'age': 30, 'city': 'London'}

# Accessing elements
print(person['name'])  # Output: Alice

# Adding elements
person['email'] = 'Kanté@chelsea.com'

# Modifying elements
person['age'] = 31

# Removing elements
del person['city']
```

### Sets
Sets in Python are unordered collections of unique elements. They are used to perform mathematical set operations such as union, intersection, difference, and symmetric difference. Sets are defined using curly braces `{}` or the `set()` constructor.

```python
# Example of sets
set1 = {1, 2, 3, 4, 5}
set2 = set([4, 5, 6, 7, 8])
```

### Set Operations
Python provides various methods and operators for performing set operations.

```python
# Example of set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1 | set2 # Union of two sets, Output: {1, 2, 3, 4, 5, 6, 7, 8}
intersection_set = set1 & set2 # Intersection of two sets, Output: {4, 5}
difference_set = set1 - set2 # Difference between two sets, Output: {1, 2, 3} 
symmetric_difference_set = set1 ^ set2 # Symmetric difference between two sets, Output: {1, 2, 3, 6, 7, 8} 
```

### Boolean Expressions
Boolean expressions in Python evaluate to either True or False. They are used in conditional statements, loops, and logical operations.Python provides various boolean operators such as `and`, `or`, and `not` for combining boolean expressions.

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