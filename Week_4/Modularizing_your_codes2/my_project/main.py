# 4. main.py
# Using the whole package
import my_package

print( my_package.add(5,3))
print(my_package.subtract(10, 4))
print(my_package.capitalize_text("python"))

# OR import specific modules
from my_package import string_utils

print(string_utils.reverse text("hello"))