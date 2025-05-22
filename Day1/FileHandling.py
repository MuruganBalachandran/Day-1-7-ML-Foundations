# -----------------------------
# File Handling in Python
# -----------------------------

# Writing to a file (overwrites if file exists)
with open("example.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is the second line.\n")

# Reading the entire content of a file
with open("example.txt", "r") as f:
    content = f.read()
    print("Full content:\n", content)

# Reading file line by line using a loop
with open("example.txt", "r") as f:
    print("Reading line by line:")
    for line in f:
        print(line.strip())  # strip() removes newline characters

# Reading single lines with readline()
with open("example.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print("First line:", line1.strip())
    print("Second line:", line2.strip())

# Reading all lines into a list with readlines()
with open("example.txt", "r") as f:
    lines = f.readlines()
    print("List of lines:", lines)

# Appending to a file (adds content without erasing)
with open("example.txt", "a") as f:
    f.write("Appending a new line.\n")

# Reading again after appending
with open("example.txt", "r") as f:
    print("After appending:")
    print(f.read())

# Using r+ mode (read and write)
with open("example.txt", "r+") as f:
    # Read the first line
    first_line = f.readline()
    print("First line using r+:", first_line.strip())

    # Write at the current position (which is after first line)
    f.write("Inserted line in the middle.\n")

# File pointer methods: tell() and seek()
with open("example.txt", "r") as f:
    print("Current file position:", f.tell())  # Start at 0
    content_part = f.read(5)  # Read first 5 characters
    print("First 5 chars:", content_part)
    print("File position after read:", f.tell())
    f.seek(0)  # Move file pointer back to start
    print("File position after seek(0):", f.tell())

# Note: Always use 'with' statement to automatically close files.
