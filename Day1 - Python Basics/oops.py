# -----------------------------
# Classes and Objects
# -----------------------------

class Dog:
    # Class variable (shared across all instances)
    species = "Canis familiaris"
    
    # Constructor / initializer
    def __init__(self, name, age):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        print(f"{self.name} says: Woof!")
    
    def get_age(self):
        return self.age
    
    # Method that uses both instance and class variables
    def info(self):
        print(f"{self.name} is {self.age} years old and belongs to species {Dog.species}.")

# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

dog1.bark()        # Buddy says: Woof!
dog2.bark()        # Lucy says: Woof!

dog1.info()        # Buddy is 3 years old and belongs to species Canis familiaris.
dog2.info()

# -----------------------------
# Inheritance
# -----------------------------

class Puppy(Dog):
    # Overriding the bark method
    def bark(self):
        print(f"{self.name} says: Yip!")

    # New method in subclass
    def weep(self):
        print(f"{self.name} is weeping.")

puppy = Puppy("Max", 1)
puppy.bark()    # Max says: Yip!
puppy.weep()    # Max is weeping.
puppy.info()    # Inherited method from Dog

# -----------------------------
# Method Overriding
# -----------------------------

# Dog.bark() prints "Woof!"
# Puppy.bark() overrides Dog.bark()

# -----------------------------
# Class Variables vs Instance Variables
# -----------------------------

print(dog1.species)   # Class variable, "Canis familiaris"
print(puppy.species)  # Inherited class variable

# Change class variable
Dog.species = "Canis lupus familiaris"

print(dog1.species)   # Updated class variable
print(puppy.species)

# Instance variable overrides class variable if set on instance
dog1.species = "Custom species"
print(dog1.species)  # Instance variable value
print(dog2.species)  # Class variable value (unchanged)

