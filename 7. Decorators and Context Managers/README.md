## Decorators and Context Managers in Python

Decorators and context managers are powerful tools for enhancing the functionality and robustness of your Python code. By leveraging decorators to modify function behavior and context managers to manage resources efficiently, you can write cleaner, more concise, and more maintainable code.

### Decorators

- **Decorators:** Decorators are functions that wrap other functions or methods to modify their behavior. They are commonly used for adding pre-processing, post-processing, or cross-cutting concerns to functions.

  ```python
  def decorator(func):
      def wrapper(*args, **kwargs):
          # Add pre-processing logic
          result = func(*args, **kwargs)
          # Add post-processing logic
          return result
      return wrapper

  @decorator
  def greet(name):
      return f"Hello, {name}!"
  ```

### Context Managers (using `with` Statement)

- **Context Managers:** Context managers allow you to manage resources and perform setup and cleanup actions automatically. They are commonly used with the `with` statement.

  ```python
  class FileManager:
      def __init__(self, filename, mode):
          self.filename = filename
          self.mode = mode

      def __enter__(self):
          self.file = open(self.filename, self.mode)
          return self.file

      def __exit__(self, exc_type, exc_value, traceback):
          self.file.close()

  with FileManager("example.txt", "r") as file:
      contents = file.read()
  ```

### Built-in Decorators and Context Managers

- **Built-in Decorators and Context Managers:** Python provides several built-in decorators and context managers, such as `@staticmethod`, `@classmethod`, `@property`, and `with open() as file`.

  ```python
  class MyClass:
      @staticmethod
      def static_method():
          pass

      @classmethod
      def class_method(cls):
          pass

      @property
      def property_method(self):
          pass
  ```

### Using Decorators and Context Managers Together

- **Using Decorators and Context Managers Together:** Decorators and context managers can be used together to create powerful and expressive code.

  ```python
  def timing(func):
      import time
      def wrapper(*args, **kwargs):
          start_time = time.time()
          result = func(*args, **kwargs)
          end_time = time.time()
          print(f"Execution time: {end_time - start_time} seconds")
          return result
      return wrapper

  @timing
  def heavy_computation():
      # Perform heavy computation
      pass

  heavy_computation()
  ```
  ---