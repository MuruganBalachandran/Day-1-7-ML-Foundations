# -----------------------------
# Comments
# -----------------------------

# This is a single-line comment

'''
This is a multi-line comment
spanning several lines
used for documentation or long explanations.
'''

# -----------------------------
# Variables and Assignment
# -----------------------------

# Integer variable
x = 10

# Float variable
pi = 3.14159

# String variable (single or double quotes work)
name = "Alice"
surname = 'Smith'

# Boolean variable
is_logged_in = True

# NoneType (represents null or no value)
nothing = None

# Multiple assignments
a, b, c = 1, 2.5, "Python"

# Same value to multiple variables
m = n = 100

# -----------------------------
# Data Types
# -----------------------------

# Integer
integer_val = 42
print(type(integer_val))  # <class 'int'>

# Float
float_val = 5.67
print(type(float_val))  # <class 'float'>

# Boolean
bool_val = False
print(type(bool_val))  # <class 'bool'>

# String
str_val = "Machine Learning"
print(type(str_val))  # <class 'str'>

# NoneType
none_val = None
print(type(none_val))  # <class 'NoneType'>

# Complex numbers (less common but used in certain math/science tasks)
complex_val = 2 + 3j
print(type(complex_val))  # <class 'complex'>

# -----------------------------
# Type Casting
# -----------------------------

# String to integer
s = "123"
converted_int = int(s)

# String to float
s2 = "45.67"
converted_float = float(s2)

# Integer to string
i = 99
converted_str = str(i)

# Float to integer (truncates the decimal part)
f = 3.99
truncated_int = int(f)  # Result: 3

# Boolean to int
true_val = int(True)   # 1
false_val = int(False) # 0

# Int to boolean
is_nonzero = bool(5)    # True
is_zero = bool(0)       # False

# -----------------------------
# print() Function
# -----------------------------

# Simple print
print("Welcome to Python Basics")

# Print multiple values
name = "Alice"
age = 25
print("Name:", name, "Age:", age)

# f-strings (recommended)
print(f"{name} is {age} years old")

# Using .format()
print("{} is {} years old".format(name, age))

# Escaping characters
print("She said, \"Hello!\"")
print('It\'s a sunny day')

# Newline and tab
print("First Line\nSecond Line")
print("Item1\tItem2\tItem3")

# -----------------------------
# input() Function
# -----------------------------

# Get user input (always returns string)
username = input("Enter your username: ")
print(f"Hello, {username}!")

# Convert input to integer
age = int(input("Enter your age: "))
print(f"You will be {age + 1} next year.")

# Convert input to float
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} m.")

# -----------------------------
# type() Function
# -----------------------------

x = 123
print(type(x))  # int

y = "hello"
print(type(y))  # str

z = 9.81
print(type(z))  # float

flag = True
print(type(flag))  # bool

empty = None
print(type(empty))  # NoneType
