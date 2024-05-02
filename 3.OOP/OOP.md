## Object-Oriented Programming (OOP) in Python

---

Object-Oriented Programming (OOP) is a programming paradigm that allows us to model real-world entities as objects with attributes (properties) and methods (behaviors). Python is an object-oriented language, which means it supports OOP principles such as encapsulation, inheritance, and polymorphism. OOP enables better code organization, modularity, and reusability, making it easier to manage and maintain large-scale projects.

# Concepts of OOP:

1. **Classes and Objects:**
   - A class is a blueprint for creating objects. It defines the attributes and methods that the objects will have.
   - An object is an instance of a class. It represents a specific instance of the class, with its own set of attributes and behaviors.

2. **Inheritance:**
   - Inheritance is a mechanism where a new class (subclass) can inherit properties and behavior from an existing class (superclass or parent class).
   - Subclasses can extend or override the functionality of the superclass.

3. **Polymorphism:**
   - Polymorphism allows objects of different classes to be treated as objects of a common superclass.
   - It enables the same method to have different implementations based on the object it is called on.

4. **Encapsulation:**
   - Encapsulation is the bundling of data (attributes) and methods that operate on the data into a single unit (class).
   - It hides the internal state of objects from the outside, and only exposes the necessary interfaces for interaction.



# Classes and Objects

In Python, a class is a blueprint for creating objects. It defines the attributes and methods that an object will have. An object is an instance of a class.

### Defining a Class

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
```

### Creating Objects (Instances)

```python
# Creating objects of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
```

## Inheritance

Inheritance allows a class (subclass) to inherit properties and methods from another class (superclass). It promotes code reuse and enables hierarchical relationships between classes.

### Defining a Subclass

```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        return f"{self.name} is studying {subject}."
```

### Creating Objects of Subclass

```python
# Creating objects of the Student class
student1 = Student("Eve", 22, "S12345")
```

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables flexibility and extensibility in the code.

### Example of Polymorphism

```python
# Function that accepts objects of different classes
def introduce(person):
    return person.greet()

# Using polymorphism
print(introduce(person1))   # Output: "Hello, my name is Alice and I am 30 years old."
print(introduce(student1))  # Output: "Hello, my name is Eve and I am 22 years old."
```

---