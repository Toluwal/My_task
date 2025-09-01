### **Python Operators**

# - Operators are special symbols in Python that perform operations on variables and values.
# Here we will focus on;

#   - Comparison Operators
  
#   - Assignment Operators

#   - Logical Operators

# **Comparison Operators**
# - Comparison operators are used to compare two values. The result is always `True` or `False`.

# | Operator | Example  | Meaning                  |
# | -------- | -------- | ------------------------ |
# | `==`     | `5 == 5` | Equal to                 |
# | `!=`     | `5 != 3` | Not equal to             |
# | `>`      | `7 > 4`  | Greater than             |
# | `<`      | `3 < 8`  | Less than                |
# | `>=`     | `6 >= 6` | Greater than or equal to |
# | `<=`     | `2 <= 5` | Less than or equal to    |

a = 10
b = 20

print(a == b)        # False

print(a != b)        # True

print(a > b)         # False

print(a < b)         # True

print(a >= 10)       # True

print(b <= 25 )      # True

# Use case Example- Student Exam Result

score = 75

print(score >= 50)      # True (passed)
print(score < 50)       # False (Failed)
print(score == 100)     # False (Not full marks)

# Assignment Operators
# - Assignment operators are used to assign values to variables. They can also combine an operation with assignment, so instead of writing `x = x + 5`, we can write x` += 5`.

# | Operator | Example   | Meaning                         |
# | -------- | --------- | ------------------------------- |
# | `=`      | `x = 10`  | Assigns value 10 to `x`         |
# | `+=`     | `x += 5`  | Adds 5 to `x` (`x = x + 5`)     |
# | `-=`     | `x -= 3`  | Subtracts 3 from `x`            |
# | `*=`     | `x *= 2`  | Multiplies `x` by 2             |
# | `/=`     | `x /= 4`  | Divides `x` by 4                |
# | `%=`     | `x %= 3`  | Stores remainder after division |
# | `**=`    | `x **= 2` | Raises `x` to the power of 2    |
# | `//=`    | `x //= 2` | Floor divides `x` by 2          |


x = 10
print("Initial value:", x)          # 10

x += 5
print("After x += 5: ", x)          # 15

x -= 2
print("After x-=2:", x)             # 13

x *= 3
print("After x *= 3: ", x)          # 39

x /= 4
print("After x /= 4:", x)           # 9.75

x %= 3
print("After x % 3:", x)            # 0.75

# Use case Example:

# Define variables
balance = 1000
deposit = 200
withdraw = 150


balance += deposit         # Add deposit
balance -= withdraw        # Subtract withdrawal

print("Updated Balance:", balance)     # 1050

# **Logical Operators**
# - Logical operators are used to combine conditional statements. They work with Boolean values (True or False).

# | Operator | Example            | Meaning                                |
# | -------- | ------------------ | -------------------------------------- |
# | `and`    | `x > 5 and x < 15` | True if both conditions are true       |
# | `or`     | `x < 5 or x > 20`  | True if at least one condition is true |
# | `not`    | `not(x == 10)`     | True if the condition is false         |


x = 10
y = 20

# and operator
print(x > 5 and y > 15)     # True

# or operator
print(x < 5 or y > 15 )     # True

# not operator
print(not(x == 10))         # False

# Use case example1 - Scholarship Eligibility

# Define variables
age = 17
score = 85

# Must be younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)
print("Scholarship eligibility: ", eligible)     # Scholarship eligibility:  True

# Use case example2 - Event Access
age = 22
has_ticket = False

can_enter = (age >= 18) and (has_ticket or age < 25)
print("Access Granted: ", can_enter)  # True (because age < 25 even without ticket )