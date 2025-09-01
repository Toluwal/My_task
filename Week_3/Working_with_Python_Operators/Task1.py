# **Task1**
# - Explain each output of the program below.
# - Give 3 usecases or scenarios where you can apply the program below.
# - Write the code for 1 of the 3 use cases.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter the second number: "))

# print(f"{num1} == {num2} : {num1 == num2}")
# output: 10 == 15 : False The output displays the integer entered and is false because num1 is not equal to num2

#print(f"{num1} != {num2} : {num1 != num2}")
# output: 10 != 15 : True  The output is false because num1 is not equal to num2

# print(f"{num1} > {num2} : {num1 > num2}")
# output: 10 < 15 : False  The output is False because num1 is not greater than num2

# print(f"{num1} < {num2} : {num1 < num2}")
# 10 < 15 : True The output is True because num1 is less than num2


# use cases 
# Case 1 : In a class room setting, It can be used to compare the ratio of females to males
# Case 2 : In an FMCG company, It can be use to compare previous month sales with the current sales or previous year and current year
# Case 3 : In a  company having attrition issues with their employers, It can be used to attritioned employees in the current year and the previous year

# Use case: FMCG Company
May = float(input("What is the total sales for juice category: "))
June = float(input("What is the total sales for juice category: "))
print(f" ₦{May}) == ₦{June} : {May == June}")      #  ₦1500000.0) == ₦1150000.0 : False

print(f" ₦{May}) != ₦{June} : {May != June}")    # ₦1500000.0) != ₦1150000.0 : True

print(f" ₦{May}) > ₦{June} : {May > June}")   #  ₦1500000.0) > ₦1150000.0 : True

print(f" ₦{May}) < ₦{June} : {May < June}")    #  ₦1500000.0) < ₦1150000.0 : False
