# -----------------------------
# Lists
# -----------------------------

# Creation
my_list = [1, 2, 3, 4, 5]

# Indexing
print(my_list[0])    # First element: 1
print(my_list[-1])   # Last element: 5

# Slicing
print(my_list[1:3])  # Elements at index 1 and 2: [2, 3]
print(my_list[:3])   # First 3 elements: [1, 2, 3]
print(my_list[2:])   # From index 2 to end: [3, 4, 5]

# Methods
my_list.append(6)           # Add at end → [1, 2, 3, 4, 5, 6]
my_list.insert(2, 99)       # Insert 99 at index 2 → [1, 2, 99, 3, 4, 5, 6]
my_list.remove(99)          # Remove 99 → [1, 2, 3, 4, 5, 6]
popped = my_list.pop()      # Remove last element → [1, 2, 3, 4, 5]
print(popped)               # 6
my_list.sort()              # Sort in ascending order
my_list.reverse()           # Reverse the list

print(my_list)              # Final list

# List comprehension
squares = [x**2 for x in range(10)]   # [0, 1, 4, 9, ..., 81]
print(squares)

# -----------------------------
# Tuples
# -----------------------------

# Immutable sequences
my_tuple = (1, 2, 3)

print(my_tuple[0])   # Access element
print(len(my_tuple)) # Length of tuple

# Tuple unpacking
a, b, c = my_tuple
print(a, b, c)

# Singleton tuple
single = (5,)
print(type(single))  # <class 'tuple'>

# -----------------------------
# Dictionaries
# -----------------------------

# Key-value pairs
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Access
print(my_dict["name"])       # Alice
print(my_dict.get("age"))    # 25

# Update/Add
my_dict["age"] = 26          # Update existing key
my_dict["email"] = "alice@example.com"  # Add new key

# Methods
print(my_dict.keys())        # dict_keys(['name', 'age', 'city', 'email'])
print(my_dict.values())      # dict_values(['Alice', 26, 'New York', 'alice@example.com'])
print(my_dict.items())       # dict_items([...])

# .update()
my_dict.update({"city": "Los Angeles", "phone": "123-456"})
print(my_dict)

# -----------------------------
# Sets
# -----------------------------

# Unordered, unique values
my_set = {1, 2, 3, 4, 2, 1}
print(my_set)  # Duplicates removed → {1, 2, 3, 4}

# Add element
my_set.add(5)

# Remove element
my_set.remove(3)  # Raises error if not found
my_set.discard(10)  # Does nothing if 10 not in set

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a | set_b)   # Union → {1, 2, 3, 4, 5, 6}
print(set_a & set_b)   # Intersection → {3, 4}
print(set_a - set_b)   # Difference → {1, 2}
print(set_a ^ set_b)   # Symmetric difference → {1, 2, 5, 6}

# Convert list to set to remove duplicates
dup_list = [1, 2, 2, 3, 4, 4]
unique = set(dup_list)
print(unique)
