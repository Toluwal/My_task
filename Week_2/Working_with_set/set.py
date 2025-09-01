# Sets in Python
# - In Python, a set is an unordered collection of unique elements. Sets are useful when you want to store multiple items but avoid duplicates.

#  Creating Sets
# 1. Using curly braces
fruits = { "apple", "banana", "mango"}
print(fruits) # {'mango', 'banana', 'apple'}

# 2. Using the set() constructor
numbers = set([1, 2, 3, 4])
print(numbers)   # {1, 2, 3, 4}

# 3. Creating an empty set ( must use set(), not {})
empty_set = set()
print(empty_set)    # set()

# 4. From a string (duplicates removed automatically)
letters = set("mississippi")
print(letters)  # {'m', 's', 'p', 'i'}

# Characteristics of Sets
# 1. Unordered: No defined indexing or sequence.

# 2. Unique elements: Duplicates are automatically removed.

# 3. Mutable: You can add or remove items.

# 4. Unindexed: You can’t access elements using an index like my_set[0].

# 5. Supports mathematical set operations: Union, intersection, difference, symmetric difference.

# Set Operations

# a. Adding Elements

colors = {"red", "blue"}
colors.add("green") 
print(colors)    # {'green', 'blue', 'red'}

# b. Removing Elements
colors.remove("blue")     # {'red', 'green'} # Removes an element, raises error if not found
print(colors)   # {'red', 'green'}
colors.discard("yellow") # Removes if found, no error if missing
print(colors) 

# c. pop an element 
colors = {"red", "blue", "green"}
#removed = colors.pop()
#print("Removed:", removed)  # Removed: red

# d. Clear a set
colors.clear()
print(colors)  # set()

# Mathematical Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 1. Union
print(set1 | set2)   # {1, 2, 3, 4, 5, 6}
print(set1.union(set2))   # {1, 2, 3, 4, 5, 6}

# 2. Intersection
print(set1 & set2)    # {3, 4}
print(set1.intersection(set2))   # {3, 4}

# 3. Difference
print(set1 - set2)    # {1, 2}
print(set1.difference(set2))   # {1, 2}

# 4. Symetric Difference
print(set1 ^ set2)   # {1, 2, 5, 6}
print(set1.symmetric_difference(set2))   # {1, 2, 5, 6}

# Working with Sets 

# Collecting unique visitors to an event

# Adding visitors 
visitors = set()

# Adding visitors
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Aisha")
visitors.add("Chinedu")  # Duplicate, ignored automatically
print("visitors:", visitors)   # visitors: {'Aisha', 'Chinedu'}

# Checking if a visitor attended
# Don't worry if you can't figure this part out yet. We figure this part out yet. We will discuss it properly later in the course.)
name = "Aisha" 
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")