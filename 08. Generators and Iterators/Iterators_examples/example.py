# Section: Iterators

''' These are some common examples of iterators in Python, showcasing different iterable objects and ways to iterate over them

'''

from itertools import count, chain, dropwhile, takewhile, permutations, combinations, cycle, groupby
from collections import deque

# Lists: Lists in Python are iterable objects
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)


# Example: Using iter() to create an iterator from a list
numbers = [1, 2, 3, 4, 5]
iter_numbers = iter(numbers)
print(next(iter_numbers))  # Output: 1
print(next(iter_numbers))  # Output: 2
print(next(iter_numbers))  # Output: 3


# Tuples: Tuples are similar to lists but are immutable
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)


# Strings: Strings are also iterable in Python
my_string = "abcdef"
for char in my_string:
    print(char)


# Dictionaries: By default, iterating over a dictionary yields its keys.
# Can be accessed .keys(), .values(), or .items() methods to iterate over keys, values, or key-value pairs respectively.
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for key in my_dict:  # Output: keys
    print(key)

for key, value in my_dict.items():  # Output: both keys and value
    print(key, value)

for keys in my_dict.keys():  # Output: keys
    print(keys)

for value in my_dict.values():  # Output: values
    print(value)


# Sets: Sets in Python are iterable objects.
my_set = set((1, 2, 3, 4, 5))  # or can be created with just {}
for i in my_set:
    print(i)


# Range: The range() function in Python returns an immutable sequence of numbers
for i in range(10):
    print(i)


# File Objects: File objects in Python are iterable
with open('file.txt', 'r') as f:
    for line in f:
        print(f"{line}\n")


# Custom Iterators: create custom iterators by implementing __iter__() and __next__() methods
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 10
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            self.current -= 1
            return self.current
        else:
            raise StopIteration

my_iter = MyIterator(0)
for i in my_iter:
    print(i)


# Enumerate: The enumerate() function is used to iterate over a sequence while keeping track of the index of each item
my_list1 = ['a', 'b', 'c', 35, 56.73]
for index, value in enumerate(my_list1):
    print(f"Index: {index}, Value: {value}")


# Zip: The zip() function is used to combine multiple iterables element-wise. 
# It returns an iterator of tuples where the i-th tuple contains the i-th element from each of the input iterables.
list1 = [1, 2, 3, 4, 5]
list2 = [11, 11, 11, 11, 11]

for i in zip(list1, list2):
    print(i)

for item1, item2 in zip(list1, list2):
    print(item1 * item2)

lista = [1, 2, 3]
listb = ['a', 'b', 'c', 'D']
for item1, item2 in zip(lista, listb):
    print(item1, item2)


# Reversed: The reversed() function returns an iterator that yields the items of a sequence in reverse order
list_before = [x for x in range(2, 31, 2)]
for item in reversed(list_before):
    print(item)


# Filter: The filter() function is used to construct an iterator from elements of an iterable for which a function returns true
def is_even(n):
    return n % 2 == 0

my_list = [x for x in range(1, 32, 3)]
for item in filter(is_even, my_list):
    print(item)


# Map: The map() function applies a given function to each item of an iterable and returns an iterator.
def square(n):
    return n * n

my_list = [x for x in range(1, 10, 2)]
for item in map(square, my_list):
    print(item)


# Generator Expressions: Generator expressions are similar to list comprehensions, but they return an iterator instead of a list.
my_gen = (x * 3 for x in range(1, 6))

for item in my_gen:
    print(item)


# Generator Functions: Generator functions use the yield keyword to return values one at a time, allowing for efficient memory usage and lazy evaluation.
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)


# Recursive Iteration: can create iterators recursively. Here's an example of a recursive iterator that generates Fibonacci numbers:
class Fibonacci:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr, self.prev = self.curr + self.prev, self.curr
        return value

fib = Fibonacci()
for num in fib:
    if num > 100:
        break
    print(num)


# Itertools: The itertools module provides a collection of functions for working with iterators. For example:
for num in count(2, 3):
    if num > 25:
        break
    print(num)


# Chain: The chain() function from itertools enables us to chain multiple iterables together as a single iterable
lista = [1, 2, 3, 4, 5, 6, 7]
listb = ['a', 'b', 'c']
a = []
for item in chain(lista, listb):
    a += [item]


# Dropwhile
nums = [x for x in range(20)]
for item in dropwhile(lambda x: x <= 5, nums):  # dropwhile returns till exhaustion of iterables
    print(item)


# Takewhile
nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 5, 3]
for item in takewhile(lambda x: x <= 5, nums1):  # takewhile only returns till the iterable evaluates to true
    print(item)


# Cycle: The cycle() function from itertools returns an iterator that repeats the elements of the input iterable indefinitely.
my_fruits_list = cycle(['Custard Apple', 'Guava', 'Mango'])
for _ in range(15):
    print(next(my_fruits_list))


# Permutations and Combinations: The permutations() and combinations() functions from itertools generate all permutations and combinations, respectively, of a given iterable
my_string = ['a', 'b', 'c', 'd']
count = 0
for perm in permutations(my_string):
    count += 1
    print(perm)
print(count)


# combinations example
for comb in combinations(my_string, 2):
    print(comb)


# Groupby: The groupby() function from itertools groups the elements of an iterable based on a key function.
data = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
grouped_data = groupby(data, key=lambda x: x[0])
for key, group in grouped_data:
    print(key, list(group))


# Deque: The deque (double-ended queue) from the collections module can be used as an iterator. It allows for efficient appending and popping of elements from both ends of the deque.
my_deq = deque([x for x in range(10)])
print(my_deq)
for item in my_deq:
    print(item)


# Filtering with List Comprehension: List comprehensions can be used to filter elements from an iterable based on a condition.
my_list = [1, 2, 3, 45, 67, 8, 98, 76, 54, 3, 22]
even_numbers = [x for x in my_list if x % 2 == 0]
for num in even_numbers:
    print(num)

