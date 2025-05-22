# -----------------------------
# Exception Handling: Catching Specific Exceptions
# -----------------------------

try:
    x = 10
    y = 0
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid value!")
except Exception as e:
    print(f"Some other error occurred: {e}")
else:
    print("Division successful:", result)
finally:
    print("This runs no matter what.")

# -----------------------------
# String Manipulation
# -----------------------------

text = "  Hello, World!  "

# String methods
print(text.lower())          # '  hello, world!  '
print(text.upper())          # '  HELLO, WORLD!  '
print(text.strip())          # 'Hello, World!'
print(text.split(','))       # ['  Hello', ' World!  ']
print(text.replace("World", "Python"))  # '  Hello, Python!  '

# -----------------------------
# String Formatting
# -----------------------------

name = "Alice"
age = 30

# f-strings (Python 3.6+)
print(f"Hello, {name}. You are {age} years old.")

# .format() method
print("Hello, {}. You are {} years old.".format(name, age))

# Positional and keyword arguments with .format()
print("Hello, {0}. You are {age} years old.".format(name, age=age))

# -----------------------------
# Multiline Strings
# -----------------------------

multiline = '''This is a
multiline string,
which spans multiple lines.'''

print(multiline)
