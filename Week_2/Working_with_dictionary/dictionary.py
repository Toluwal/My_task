## **Python Dictionaries**
# - A dictionary in Python is a collection of key-value pairs.

#   - **Keys** are unique and used to store and retrieve values.

#   - **Values** can be any data type (string, integer, list, tuple, even another dictionary).

#synax
#dictionary_name = {key1: value1, key2: value2}

# **Characteristics of Dictionaries**

# 1. **Key-Value Structure**: Each item is stored as a key: value pair.

# 2. **Mutable**: You can add, change, or remove items.

# 3. **Unordered (before Python 3.7)**:  From Python 3.7+, they maintain insertion order.

# 4. **Unique Keys**:  No duplicate keys allowed; a new assignment to an existing key overwrites the old value.

# 5. **Keys must be immutable**:  Strings, numbers, tuples (containing only immutable items) can be keys.


# Creating Dictionaries
# 1. Using curly braces
student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}
print(student)    # {'name': 'Ada', 'age': 20, 'course': 'Computer Science'}

# Using the dict() constructor
student_info = dict(name= "John", age=25, course="Maths")
print(student_info)   # {'name': 'John', 'age': 25, 'course': 'Maths'}

# 3. Empty dictionary
empty_dict = {}
print(empty_dict)   # {}

# Add key-value pairs to it
student = {}
student["name"] = "Goodness"
student["Interest"] = "AI"
student ["Track"] = " AI_Dev"
print(student)

# List of dictionaries - each student has their own dictionary

students = [
    {"Name": "John", "Interest": "Cloud Computing", "Track": "AI_Eng"},
    {"Name": "Paul", "Interest":"Cyber Security", "Track": "AI_Dev"}
]

print(students[0]["Name"])  # John
print(students[1]["Track"]) # AI_Dev

# Dictionary of dictionaries - Each student is keyed by their ID

students = {
    "AI010" : {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},"AI020": {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
    "AI030" : {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev" }
}
print(students["AI020"]["Name"])   # Mary
print(students["AI030"]["Track"])  # AI_Dev

# Dictionary of lists - Each subject stores a list of scores

scores = {
    "python": [85, 78, 92],
    "pandas": [88, 74, 90],
    "Scikit-learn": [80, 95, 87]
}

print(scores["python"])    # [85, 78, 92]
print(scores["pandas"][1])  # 74

# 4. Dictionary Comprehension

# Syntax:`{key_expression: value_expression for item in iterable if condition}`

# Create a dictionary of numbers and their squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With Condition
# Dictionary of even numbers and their cubes
evens_cube = {x: x**3 for x in range(1, 10) if x % 2 ==0}
print(evens_cube)   # {2: 8, 4: 64, 6: 216, 8: 512}

# From Existing Dictionary
students = {"Ada": 85, "John": 40, "Musa": 65}

# Filter students who passed (score >= 50)
passed_students = {name: score for name, score in students.items() if score >= 50}
print(passed_students)  # {'Ada': 85, 'Musa': 65}

# Using String Keys
names = ["Ada", "John", "Musa"]
lengths = {name: len(name) for name in names}
print(lengths)    # {'Ada': 3, 'John': 4, 'Musa': 4}

# Accessing Dictionary Items

# define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}  # 'Ada': 3, 'John': 4, 'Musa': 4}

# Using Key
print(student["name"])    # Ada

# Using get() method (avoid error if key is missing)
print(student.get("age"))                  # 20
print(student.get("grade", "Not found"))   # Not found
# Modifying Dictionaries

student["age"] = 21  # Change value 
student["grade"] = "A" # Add new key-value pair
print(student)  # {'name': 'Ada', 'age': 21, 'course': 'Computer Science', 'grade': 'A'}

# **Removing Items from Dictionaries**

# 1. using pop()  # deletes what is specified
student.pop("grade")
print(student)      # {'name': 'Ada', 'age': 21, 'course': 'Computer Science'}

# # 2. Using popitem() - removes last inserted key-value
student.popitem()
print(student)       # 'name': 'Ada', 'age': 21}

# # 3. Using del keyword
del student["age"]
print(student)    # {'name': 'Ada'}

# Using clear() - removes all items
student.clear()
print(student)   # {}

# Dictionary Methods
# dot keys(), dot values(), dot(items), dot update()

person = {"name": "Emeka", "age":30}

# 1. keys()
print(person.keys())  # dict_keys(['name', 'age'])

# 2. values()
print(person.values())  # dict_values(['Emeka', 30])

# 3. items()
print(person.items())    # dict_items([('name', 'Emeka'), ('age', 30)])

# 4. update()
person.update({"age": 31, "city": "Lagos"})
print(person)   # {'name': 'Emeka', 'age': 31, 'city': 'Lagos'}

students = {
    "student1": {"name": "Ada","age": 20},
    "student2": {"name": "John", "age": 22}
}

print(students["student1"]["name"])  # Access nested data # Ada

# Looping through Dictionaries
# Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}

# Loop through keys
for key in student:
    print(key)  # name age course

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")   # name: Ada age: 20 course: Computer Science

# Storing a student's biodata
student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"], "is_full_time": True

}

print(f"Name: {student['name']}")  # Name: Chinedu
print(f"Subjects: {', '.join(student['subjects'])}")  # Subjects: Maths, Physics, Chemistry

# **Final Thought**
# Storing a student's biodata
# student = {
#     "name": "Chinedu",
#     "age": 19,
#     "department": "Engineering",
#     "subjects": ["Maths", "Physics", "Chemistry"],
#     "is_full_time": True
# }

# print(f"Name: {student['name']}")
# print(f"Subjects: {', '.join(student['subjects'])}")

