1. What is python?

    - Python is an high level, interpreted programming language with dynamic semantics, known for ease of learning and readbilitty

2. what are the key features of Python?
    
    - easy to read syntax, dynamic typing,memory management, comprhensive standard library

3. how is memory managed in python?

    - memory in python is managed by python memory manager, objects and data structures are stored in a private heap and the garbage collector recycles unused memory

4. what are decorators in python?

    - decorartors are a design pattern in Python that allows users to modify the behaviour of Function or class
    - Decorators are a powerful tool in Python for implementing cross-cutting concerns, such as logging, authentication, caching, and more, in a modular and reusable way.

5. what is PEP 8?

    - PEP 8 is the python enhancement protocal that provides guidlines and best practices on how to write a python code

6. whatt is a lambda function in python?

    - A lambda function is a small anonymous function that can take any number of arguments but only have one expression

7. what is the difference between a tuple and a list?

    - lists are mutable
    - tuples are immutable

8. how do python handle memory deallocation?

    - python has a  builtin garbage collector which recycles all the unused memory so that it can be made available for the heap space

9. what is slicing in python?

    - slicing in python is a mechanism to select a range of items from sequence types such as list, ttuple, strings etc.

10. what are pyhton modules?

    - python models are .py files that consist of python code. any python file can reference as a module

11. what is the difference between a python arrays and lists?

    - arrays can only contain elements of same data type, while list can contain elemnts of different data types.

12. what is the difference between deepcopy and copy?

    - deepcopy creates a new compound object and then recursively inserts copies into it of the objects found in the original
    - copy creates a new compound object and then insets references into it to the objects found in the original

13. what is a namespace in python?
    
    - A namespace is a naming system used to ensure that names are unique to avoid naming conflicts

14. what is a dictionary in python?

    - a dictionary in python is an unordered collection of data values used to store data values like a map

15. what is the difference between xrange and a range?

    - xrange retturns the xrange object and uses the same memory location
    - range returns a list

16. what is pickling and unpickling?

    - pickling is a process wherby a python object heirarchy is converted into byte stream and unpickling is the inverse operation

17. what are python genarators?

    - generators are a simple way of calling iterators. they return a lazy iterator that can be looped through

18. what is __init__?

    - __init__ is a metthod or constructor in python. this method is automatically called to allocatte memory when a new instance/object of a class is created

19. what is __str__?

    - __str__ is a built in function in python that is called when the following functions are invoked on the objectt
        - print()
        - str()

20. what is the difference between append() and extend() methods?

    - append() adds its argument as a single element to the end of a list
    - extend() adds each elemnt of of the argument to the list

21. whatt is a docstring in python?

    - a docstring is a string literal that occurs as the first statement in a module, function, class or method defination

22. what is self in python?

    - self represents the instance of the class and binds the attributes with the given arguments

23. what is the difference between local and global variables?

    - global variables are accesible through out the program
    - local variables are only accesible within tthe scope of the function where they are declared

24. what is the pass statemnt in python?

    - the pass statement is a null operation. nothing happens when it executes

25. what is the difference between == and 'is' ?

    - == checks for equality
    - 'is' checks for identity

26. what is a session in python?

    - a session allows you to persist certain parameters across requests

27. what is the difference between break, continue and pass?

    - break terminates the loop
    - continue skipy the current iteration
    - pass does nothing and acts as a placeholder

28. what is *args and **kwargs?

    - *args is used to pass variable number of arguments to the function
    - **kwargs allows user to pass keyword variable length of arguments to the function

29. what is the difference between isinstance and type()?

    - isinstance() checks if an object is insttance of a class or a subclass
    - type() returns the type of the object

30. what is the difference between .py and .pyc files?

    - .py files contain the source code of the program
    - .pyc files contain the bytecode which can be executed by the python virtual machine

31. what is __name__ in pyhton?

    - __name__ is a built in variable which evaluates the name of the current module

32. what are metaclasses in python?

    - metaclasses are classes of classes othat define how a class behaves

33. what is monkey patching in python?

    - monkey patching is a technique to add, modify or suppress the behaviour of a piece of code at runtime

34. what is the with statement in python?

    - the with statement simplifies exception handling by encapsulating common preparation and cleanup tasks in so called context managers

35. what is hte difference between staticmethod and classmethod?

    - staticmethod doesnt recieve an impicit first argument 
    - classmethod recieves the class as an implict first argument

36. what is hte difference between .py files and .pyw files?

    - .py are source code files
    - .pyw are python script files meant to be run on the windows platform without opening a comand prompt window

37. what is the difference between assert and raise?

    - assert is used for debugging purposes
    - raise is used to raise exceptions

38. what is the enumerate function in python?

    - ennumerate is a built in function that adds a counter to an iterable and returns it in a form of enumerate object

39. what is the difference between __new__ and __init__?

    - __new__ is a static method that is called to create an instance
    - __init__ is a constructor is called to initialize an instance

40. what is the differenc between __getattr__ and __getattribut__?

    - __getattr__ is called when an attribute lookup has not found in the attribute in the usual places
    - __getattribute__ is called before looking at the actual attributes on the object

41. what is the global keyword in python?
    
    - the global keyword is used to declare that a variable inside the function is global(outside th function)

42. what is the differenc between __call__ and __init__?
    
    - __call__ allows an instance of a class to be called as a function
    - __init__ initializes a instance of a class

43. whatt is the difference between __dict__ and __dir__?

    - __dict__ is a dictionary or other mapping object used to store an objects attributes
    - __dir__ is used to list attributes of the object

44. what is the super function in python?

    - super is used to give acess to methods and properties of a  parent or sibling class

45. what is the difference between __str__ and __repr__?

    - __str__ is used for creating output for te end user
    - __repr__ is used for debugging and development. __repr__ is more precise and clear than __str__

46. what is the zip function in python?

    - zip is a built in function that returns the iterator of tuples based on the iterable objects

47. what are unit tests in python?
    
    - unit tests are tests written to check the functionallity of the specific section of code, usually at the function level

48. what is the Global interpreter lock in python?

    - GIL is a mutex that protects access to python objects, preventing multiple threads from executing python bytecodes at once

49. what are function annotations in python?

    - Function annotations provide a way of associating various parts of a function with arbitary python expressions at compile time.

 