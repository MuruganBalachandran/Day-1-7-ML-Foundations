# -----------------------------
# Arithmetic Operators
# -----------------------------

a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division (float): 3.333...
print(a // b)  # Floor Division: 3
print(a % b)   # Modulus: 1 (remainder)
print(a ** b)  # Exponentiation: 10^3 = 1000

# -----------------------------
# Comparison Operators
# -----------------------------

x = 5
y = 8

print(x == y)   # Equal: False
print(x != y)   # Not equal: True
print(x > y)    # Greater than: False
print(x < y)    # Less than: True
print(x >= 5)   # Greater than or equal to: True
print(x <= 4)   # Less than or equal to: False

# -----------------------------
# Logical Operators
# -----------------------------

is_sunny = True
is_warm = False

print(is_sunny and is_warm)  # False: both must be True
print(is_sunny or is_warm)   # True: at least one is True
print(not is_sunny)          # False: negation

# -----------------------------
# Assignment Operators
# -----------------------------

z = 10       # Basic assignment
z += 5       # z = z + 5 → 15
z -= 3       # z = z - 3 → 12
z *= 2       # z = z * 2 → 24
z /= 4       # z = z / 4 → 6.0

print(z)

# -----------------------------
# Membership Operators
# -----------------------------

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)     # True
print("grape" not in fruits)  # True

text = "machine learning"

print("learn" in text)        # True
print("deep" not in text)     # True

# -----------------------------
# Identity Operators
# -----------------------------

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is c)        # True (same object)
print(a is b)        # False (different objects with same content)
print(a == b)        # True (same content)

print(a is not b)    # True
print(a is not c)    # False
