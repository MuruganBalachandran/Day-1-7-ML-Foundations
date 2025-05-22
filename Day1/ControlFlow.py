# -----------------------------
# Conditional Statements
# -----------------------------

age = 18

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# Nested if example
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    if score >= 85:
        print("Grade: B+")
    else:
        print("Grade: B")
else:
    print("Grade: C or below")

# -----------------------------
# for Loops
# -----------------------------

# Loop over a range of numbers
for i in range(5):
    print(f"Number: {i}")

# Loop over a list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# Nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

# -----------------------------
# while Loops
# -----------------------------

count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Infinite loop with break
x = 0
while True:
    if x >= 3:
        break
    print("x =", x)
    x += 1

# -----------------------------
# break, continue, pass
# -----------------------------

# break: exits the loop
for i in range(10):
    if i == 5:
        break
    print("Break Example:", i)

# continue: skips to next iteration
for i in range(5):
    if i == 2:
        continue
    print("Continue Example:", i)

# pass: does nothing (placeholder)
for i in range(3):
    pass  # Used when the loop body is yet to be implemented

# -----------------------------
# range() Function
# -----------------------------

# range(stop)
for i in range(3):  # 0, 1, 2
    print("range(stop):", i)

# range(start, stop)
for i in range(2, 5):  # 2, 3, 4
    print("range(start, stop):", i)

# range(start, stop, step)
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print("range(start, stop, step):", i)

# -----------------------------
# enumerate()
# -----------------------------

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# -----------------------------
# zip()
# -----------------------------

names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 92]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
