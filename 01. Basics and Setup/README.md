## Python Fundamentals:

**Python Overview:**
   - Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility. It finds applications in web development, data analysis, AI, scientific computing and more. Its popularity is driven by a large standard library, active community, and support for various programming paradigms.

**Python 2 vs. Python 3:**
   - Python 3 introduced backward-incompatible changes compared to Python 2, addressing issues and enhancing consistency. Notable differences include:
     - Print Statement: Python 2 uses `print`, Python 3 uses `print()` function.
     - Unicode: Python 3 treats strings as Unicode by default.
     - Division: Python 3 defaults to floating-point division, while in Python 2, it performs integer division unless specified otherwise.

**Key Features:**
   - Python's features include:
     - Simple and easy-to-read syntax
     - Dynamic typing and automatic memory management
     - Rich data structures
     - Extensive standard library
     - Interpreted nature, allowing for rapid development and prototyping
     - Support for multiple programming paradigms (procedural, object-oriented, functional, etc.)

**Installation Steps:**
   - Download the Python installer from [python.org](https://www.python.org/).
   - Run the installer, ensuring to add Python to PATH.
   - Verify installation via terminal or command prompt with `python --version` or `python3 --version`.
   - Consider installing a code editor/IDE for better development experience.
   - consider setting up virtual environments using `venv` or `virtualenv`.
   - To create a virtual environment with `venv`, navigate to your project directory in the terminal and run:

   ```
   # This command creates a new virtual environment named "env" in the current directory.
   python -m venv env

   # To Activate the virtual environment On Windows
   .\env\Scripts\activate

   # To Activate the virtual environment On macOS or Linux
   source env/bin/activate 
   ```

**Running Python Code:**
   - Run Python code through:
     - Interactive Interpreter in command-line interface (CLI)/terminal
     - Script Execution from CLI/terminal
     - Integrated Development Environments (IDEs) like PyCharm, VSCode, or Jupyter Notebook.

---