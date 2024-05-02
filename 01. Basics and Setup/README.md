## Python Fundamentals:

1. **What is Python and why use Python?**
   - Python is a high-level, interpreted programming language known for its simplicity and readability. It is popular for its versatility, as it can be used for various purposes such as web development, data analysis, artificial intelligence, scientific computing, and more. Python's popularity also stems from its large standard library, active community, and support for multiple programming paradigms.

2. **Explain the differences between Python 2 and Python 3.**
   - Python 2 and Python 3 are two major versions of the Python programming language. Python 3 was introduced as a backward-incompatible upgrade to Python 2, addressing various shortcomings and improving the language's consistency. Some key differences include:
     - Print Statement: Python 2 uses the `print` statement, while Python 3 uses the `print()` function.
     - Unicode: Python 3 treats strings as Unicode by default, while Python 2 treats strings as ASCII.
     - Division: In Python 3, division of integers produces floating-point results by default, while in Python 2, it performs integer division unless specified otherwise.

3. **What are the key features of Python?**
   - Key features of Python include:
     - Simple and easy-to-read syntax
     - Dynamic typing and automatic memory management
     - High-level data structures
     - Extensive standard library
     - Interpreted nature, allowing for rapid development and prototyping
     - Support for multiple programming paradigms (procedural, object-oriented, functional, etc.)

4. **How do you install Python?**
    To install Python, follow these steps:

    1. **Download Python Installer:**
    - Visit the official Python website at https://www.python.org/.
    - Navigate to the "Downloads" section.
    - Choose the appropriate installer for your operating system. Python is available for Windows, macOS, and Linux.

    2. **Run the Installer:**
    - Once the installer is downloaded, run the executable file.
    - Follow the prompts in the installation wizard.
    - Make sure to check the option "Add Python to PATH" during installation. This allows you to run Python from the command line without specifying the full path.

    3. **Complete the Installation:**
    - After completing the installation process, Python should be installed on your system.
    - You can verify the installation by opening a terminal or command prompt and typing `python --version` or `python3 --version`. This command will display the installed Python version.

    4. **(Optional) Install a Code Editor or IDE:**
    - While Python comes with its own interactive interpreter and a basic text editor (IDLE), you may prefer to use a dedicated code editor or integrated development environment (IDE) for writing Python code.
    - Popular choices include Visual Studio Code, PyCharm, Sublime Text, Atom, and Jupyter Notebook.

    5. **(Optional) Set Up a Virtual Environment:**
    - It's good practice to set up a virtual environment for each Python project to manage dependencies and isolate project environments.
    - You can create a virtual environment using the `venv` module (for Python 3) or `virtualenv` package (for Python 2 and 3).
    - To create a virtual environment with `venv`, navigate to your project directory in the terminal and run:
        ```
        python -m venv env
        ```
        This command creates a new virtual environment named "env" in the current directory.
    - Activate the virtual environment:
        - On Windows:
        ```
        .\env\Scripts\activate
        ```
        - On macOS and Linux:
        ```
        source env/bin/activate
        ```
5. **How do you run Python code?**

   Python code can be run using various methods:

   * Interactive Interpreter (command-line): Enter python in the terminal to open the Python interpreter and execute code interactively.
   * Script Execution: Save Python code in a file with a .py extension and run it using the command python filename.py.
   * Integrated Development Environments (IDEs): Use IDEs like PyCharm, VSCode, or Jupyter Notebook for writing, executing, and debugging Python code.






4. **How does Python handle error and exceptions?**
   - Python provides a robust mechanism for handling errors and exceptions through `try`, `except`, `finally`, and `raise` statements. 
   - You can use a `try` block to wrap the code that may raise exceptions, and `except` block(s) to handle specific exceptions or to catch all exceptions.
   - The `finally` block is executed regardless of whether an exception occurs or not and is often used for cleanup actions.
   - You can also use the `raise` statement to raise your own exceptions when certain conditions are met.

5. **How are arguments passed in Python: by value or by reference?**
   - Arguments in Python are passed by object reference. This means that when you pass an object (like a list or a dictionary) to a function, you are passing a reference to that object. Any modifications made to the object within the function will affect the original object outside the function.
   - However, for immutable objects (like integers, strings, and tuples), the behavior appears similar to pass by value, as changes made to these objects within a function do not affect the original objects outside the function.
