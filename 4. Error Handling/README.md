## Error Handling and Exception Management in Python

- Error handling and exception management are essential aspects of Python programming to handle unexpected errors and exceptions gracefully. Python provides robust mechanisms for identifying, handling, and raising exceptions.

- By using try-except blocks, handling multiple exceptions, and defining custom exception classes, you can effectively manage errors and ensure smooth execution of your programs.

### Try-Except Blocks

- **Try-Except Blocks:** A `try` block is used to wrap code that may raise exceptions, while one or more `except` blocks catch and handle specific types of exceptions.

  ```python
  try:
      # Code that may raise an exception
      result = 10 / 0
  except ZeroDivisionError:
      # Handle specific exception
      print("Error: Division by zero!")
  ```

### Handling Multiple Exceptions

- **Handling Multiple Exceptions:** Multiple `except` blocks can be used to handle different types of exceptions.

  ```python
  try:
      file = open("file.txt", "r")
      contents = file.read()
      file.close()
  except FileNotFoundError:
      print("Error: File not found!")
  except IOError:
      print("Error: Unable to read file!")
  ```

### Else and Finally Blocks

- **Else Block:** An `else` block is executed if no exceptions occur in the `try` block.
- **Finally Block:** A `finally` block is always executed, regardless of whether an exception occurs or not. It is often used for cleanup actions.

  ```python
  try:
      file = open("file.txt", "r")
      contents = file.read()
  except FileNotFoundError:
      print("Error: File not found!")
  else:
      print("File contents:", contents)
  finally:
      if 'file' in locals():
          file.close()
  ```

### Raising Exceptions

- **Raising Exceptions:** You can raise exceptions using the `raise` statement to indicate error conditions in your code.

  ```python
  x = -5
  if x < 0:
      raise ValueError("Invalid value: x must be non-negative")
  ```

### Custom Exception Classes

- **Custom Exception Classes:** You can define custom exception classes by subclassing built-in exception classes or the Exception base class.

  ```python
  class CustomError(Exception):
      pass
  
  try:
      # Code that may raise CustomError
      raise CustomError("Something went wrong")
  except CustomError as e:
      print("Custom error:", e)
  ```
---