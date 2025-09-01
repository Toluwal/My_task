# my_module/main.py

import first
import second

# lets use the functions in the first.py file


print("=== Math Functions ===")
print("5 + 3 =", first.add(5,3))   # 5 + 3 = 8
print("10 - 4 =", first.subtract(10, 4)) # 10 - 4 = 6
print("6 * 7 =", first.multiply(6, 7))   # 6 * 7 = 42
print("20 / 5 =", first.divide(20, 5))   # 20 / 5 = 4.0

# Lets use the functions in the second.py file
print("\n=== String Functions ====")
print(second.greet("Ridwan"))     # Hello, Ridwan!  I am creating my own module
print("Reverse of 'Python' =", second.reverse_string("Python"))    # Reverse of 'Python' = nohtyP
print("Character count in sentence =", second.count_characters("Python modules are powerful"))    # Character count in sentence = 27
print("Word count in sentence =", second.count_words("Python modules are powerful"))      # Word count in sentence = 4

