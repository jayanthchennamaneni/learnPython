# Functional Programming Techniques in Python

Functional programming is a paradigm that emphasizes the evaluation of mathematical functions and avoids changing state and mutable data. Python, while primarily object-oriented, supports functional programming techniques through features like lambda functions, map, filter, and reduce functions.


## **Lambda Functions:**
    - These are small, inline functions defined using the `lambda` keyword.

```python
# Syntax: lambda arguments: expression
square = lambda x: x ** 2
```

## **Map Function:** 
    - Applies a given function to each item in an iterable and returns an iterator of the results.

```python
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x ** 2, numbers) # 'squares' will be a map object (iterator).You can use it in a loop, or you can convert it to a list or any other iterable data structure if you want to see its contents.
squares_list = list(squares) # output: [1, 4, 9, 16, 25]
```

## **Filter Function:** 
    - Applies a given predicate function to each item in an iterable and returns items for which the function returns `True`.

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
even_numbers_list = list(even_numbers) # output: [2, 4]
```

## **Reduce Function:** 
    - Applies a binary function to the items of an iterable, cumulatively, from left to right, to reduce the iterable to a single value.

```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers) # x and y in the lambda function represent consecutive elements from the list, and at each step, they are updated to the result of the previous operation and the next element from the list, respectively.
```

## **List Comprehensions:** 
    - Provide a concise way to create lists based on existing lists or iterables.

```python
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
```

## **Generator Expressions:** 
    - Similar to list comprehensions but return a generator object, generating values lazily, one at a time.

```python
numbers = [1, 2, 3, 4, 5]
squares_generator = (x ** 2 for x in numbers)
```

Functional programming techniques in Python offer concise and expressive ways to manipulate data and perform computations, enhancing code readability and maintainability.

---