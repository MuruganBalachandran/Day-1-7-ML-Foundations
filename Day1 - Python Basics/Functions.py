# -----------------------------
# Defining Functions
# -----------------------------

def greet():
    print("Hello, world!")

greet()  # Call the function

# -----------------------------
# Parameters and Return Values
# -----------------------------

def add(a, b):
    result = a + b
    return result

sum_val = add(3, 4)
print("Sum:", sum_val)

# -----------------------------
# Default Arguments
# -----------------------------

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")     # Hello, Alice!
greet()            # Hello, Guest!

# -----------------------------
# *args (Variable Positional Arguments)
# -----------------------------

def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3)
print_numbers(10, 20)

# args is a tuple

# -----------------------------
# **kwargs (Variable Keyword Arguments)
# -----------------------------

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")

# kwargs is a dictionary

# -----------------------------
# Lambda Functions (Anonymous Functions)
# -----------------------------

square = lambda x: x ** 2
print(square(5))  # 25

multiply = lambda a, b: a * b
print(multiply(3, 4))  # 12

# Used often in higher-order functions like map, filter, reduce

# -----------------------------
# map() Function
# -----------------------------

nums = [1, 2, 3, 4]

# map applies a function to each item in a list
squared = list(map(lambda x: x**2, nums))
print("Squared:", squared)

# -----------------------------
# filter() Function
# -----------------------------

# filter returns items for which the function returns True
even = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even)

# -----------------------------
# reduce() Function
# -----------------------------

from functools import reduce

# reduce applies a rolling computation to pairs of items
sum_all = reduce(lambda x, y: x + y, nums)
print("Sum using reduce:", sum_all)

product_all = reduce(lambda x, y: x * y, nums)
print("Product using reduce:", product_all)
