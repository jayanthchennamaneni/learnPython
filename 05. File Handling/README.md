## File Handling and Input/Output Operations in Python

File handling and input/output (I/O) operations are fundamental tasks in Python for interacting with files. Python provides built-in functions and methods to perform various file operations efficiently.

### Opening and Closing Files

**Opening Files:** Use the `open()` function to open a file in different modes such as read mode `'r'`, write mode `'w'`, or append mode `'a'`.

```python
# Open a file in read mode
file = open("example.txt", "r")
```

**Closing Files:** After performing file operations, it's important to close the file using the `close()` method to release system resources.

```python
file.close()
```

### Reading from Files

**Reading Entire File:** Use the `read()` method to read the entire contents of the file as a single string.

```python
contents = file.read()
```

**Reading Line by Line:** Use a loop to iterate over each line in the file using the `readline()` method.

```python
line = file.readline()
```

### Writing to Files

**Writing to Files:** Open a file in write mode `'w'` or append mode `'a'` and use the `write()` method to write data to the file.

```python
# Open a file in write mode
file = open("output.txt", "w")
file.write("Hello, world!\n")
```

**Writing Multiple Lines:** Use the `writelines()` method to write a list of strings to a file.

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file.writelines(lines)
```

### Input/Output Operations

**Reading User Input:** Use the `input()` function to prompt the user for input from the console.

```python
name = input("Enter your name: ")
```

**Printing to the Console:** Use the `print()` function to output data to the console.

```python
print("Hello, world!")
```

### Using Context Managers (with Statement)

**Using Context Managers:** Use the `with` statement to automatically handle opening and closing of files, ensuring proper resource management.

```python
with open("example.txt", "r") as file:
    contents = file.read()
# File automatically closed after exiting the block
```
### Error Handling

**Error Handling:** Handle file-related errors using try-except blocks to ensure robustness and graceful error handling.

```python
try:
    file = open("example.txt", "r")
    contents = file.read()
except FileNotFoundError:
    print("Error: File not found!")
finally:
    file.close()  # Ensure file is closed even if an error occurs
```

These file handling and I/O operations are essential for working with external data sources and interacting with users in Python applications.

---