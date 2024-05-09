# Section: Generators

''' In all these examples, the key concept is the use of the yield keyword, 
    which turns a regular function into a generator function. When the function is called, 
    it returns a generator object that can be iterated over to produce the sequence of values.'''

import random
from itertools import permutations 

# Counting numbers generators: which yields numbers from 1 up to n
def count_upto(n):
    count = 1           
    while count <= n:   
        yield count     
        count += 1      

for num in count_upto(5):  
    print(num) 


# Fibonacci Sequence Generator: to generate Fibonacci sequence
def fibonacci():
    a, b = 0, 1        
    while True:         
        yield a        
        a, b = b, a + b  

fib = fibonacci()       
for _ in range(10):     
    print(next(fib))    


# Custom Range Function Generator: to generate numbers within a custom range
def custom_range(start, stop, step=1):
    while start < stop:     
        yield start         
        start += step       

for num in custom_range(1, 10, 2):  
    print(num)                      


# Infinite Sequence Generator: to generate an infinite sequence of numbers
def infinite_sequence(): 
    num = 0         
    while True:     
        yield num   
        num += 1    

gen = infinite_sequence()  
for _ in range(5):         
    print(next(gen))       


# Filtering Generator: to generate an infinite sequence of even numbers
def even_numbers():
    num = 0                 
    while True:             
        if num % 2 == 0:    
            yield num       
        num += 1          

evens = even_numbers()  
for _ in range(5):      
    print(next(evens))

# Generator Expression
cube_gen = (x**3 for x in range(1, 10))  # Create a generator expression to generate cubes of numbers from 1 to 9
for cube in cube_gen:  
    print(cube)

# Generator with Conditional Logic: to filter numbers based on a condition
def filter_numbers(numbers, condition):
    for num in numbers:  
        if condition(num):  
            yield num  

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_num = filter_numbers(numbers, lambda x: x % 2 == 1)
for num in odd_num: 
    print(num)

# Combining generators to combine the outputs of two input generators
def combined_generator(gen1, gen2):
    for val in gen1: 
        yield val 
    for val in gen2:  
        yield val 

gen1 = (x for x in range(1, 4))  
gen2 = (x for x in range(4, 7))  
combined_gen = combined_generator(gen1, gen2) 

for val in combined_gen:  
    print(val)
 

# Permutations: A generator function to generate all permutations of characters in the input string
def permute_string(input_str):
    for perm in permutations(input_str):  
        yield ''.join(perm)              

for permuted_str in permute_string('abc'):  
    print(permuted_str) 

# Prime number generator: A generator to print the first n prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

prime_gen = prime_generator()
for _ in range(10):
    print(next(prime_gen))

# Generator with State that yields consecutive integer values starting from 0 and increments the state with each iteration.
def stateful_generator():
    state = 0  
    while True:  
        yield state  
        state += 1  

gen = stateful_generator()  
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2


# Generator with Error Handling: that attempts to perform division and yields the result. If a division by zero error occurs, it yields an error message instead.
def safe_divide(a, b):
    try:
        yield a / b  
    except ZeroDivisionError:
        yield "Error: Division by zero"  

div_gen = safe_divide(10, 0) 
print(next(div_gen))


# Generator for Random Data: that yields random integers between 1 and 100 indefinitely.
def random_data_generator():
    while True:  
        yield random.randint(1, 100)

rand_gen = random_data_generator()  
for _ in range(5): 
    print(next(rand_gen))


# Factorials generator: that generates factorials of consecutive integers starting from 1.
def factorial_generator():
    num = 1 
    fact = 1  
    while True:  
        yield fact  
        num += 1  
        fact *= num  

fact_gen = factorial_generator() 
for _ in range(6): 
    print(next(fact_gen))


# Generator for Collatz Sequence: that generates the Collatz sequence for a given integer n.
def collatz_sequence(n):
    while n != 1:  
        yield n  
        n = n // 2 if n % 2 == 0 else 3 * n + 1  # Update n according to the Collatz rule
    yield 1 

for num in collatz_sequence(7):  
    print(num)





















