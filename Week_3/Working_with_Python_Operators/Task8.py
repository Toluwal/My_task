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
# May = float(input("What is the total sales for juice category: "))
# June = float(input("What is the total sales for juice category: "))
# print(f" ₦{May}) == ₦{June} : {May == June}")      #  ₦1500000.0) == ₦1150000.0 : False

# print(f" ₦{May}) != ₦{June} : {May != June}")    # ₦1500000.0) != ₦1150000.0 : True

# print(f" ₦{May}) > ₦{June} : {May > June}")   #  ₦1500000.0) > ₦1150000.0 : True

# print(f" ₦{May}) < ₦{June} : {May < June}")    #  ₦1500000.0) < ₦1150000.0 : False


# **Task2**
# - Comment the code below appropriately, and using doctring, explain what the code is doing.
# -  Adapt the code to the case below.

# - Federal Government Scholarship Key Eligibility Requirements:
#   - Citizenship:
#     - Applicant must be a citizen of Nigeria. 
#   - Enrollment:
#     - Must be a registered, full-time undergraduate student in a recognized Nigerian university. 
#   - Other Scholarships:
#     - Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. 
#   - Academic Qualification:
#     - For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.

# 
# citizenship = input("Country of citizenship: ")
# enrollment = input("Are you a registered full-time undergraduate student in a recognized Nigerian_university?: ")
# other_scholarship = input("Are you a current recipient of Oil and Gas industry, whether national or international?:  ")
# academic_qualification = input("Do you have 5 As and Bs in relevants subjects including English and Mathematics")

# eligibility = ((citizenship == "Nigeria") or (citizenship == "Nigerian")) and (enrollment == "Yes") and (other_scholarship) != "Yes " and (academic_qualification == "Yes")

# print(f"\nEligibility Requirements: \nCitizenship: {citizenship}\nEnrollment status: {enrollment}\nOther scholarships: {other_scholarship}\nAcademic Qualification: {academic_qualification}\nEligible: {eligibility}")

# Eligibility Requirements:
# Citizenship: Nigeria
# Enrollment status: Yes
# Other scholarships: No
# Academic Qualification: Yes
# Eligible: True


# - Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).

# - Start with an empty cart total (cart_total = 0).

# - Use assignment operators (+=) to add the price of some items into cart_total.

# - Print the list of items and the total price using an f-string like this:
# ```
# Items: ['Book', 'Pen', 'Bag']
# Total Price: ₦600


# items = ["shoe", "clothes", "bag", "wrist-watch", "necklace", "wristband"]
# price = [ 15000, 20500, 25000, 12000, 15000, 50000]
# cart_total = 0
# cart_total += price[0] 
# cart_total += price[1] 
# cart_total+= price[2]
# cart_total+=price[3]
# cart_total+=price[4]
# cart_total+=price[5]

# print(f"Items: {items}\nTotal price: ₦{cart_total}")

# Items: ['shoe', 'clothes', 'bag', 'wrist-watch', 'necklace', 'wristband']
# Total price: ₦137500


# **Task4: Student Record**
# - Create an empty dictionary called student.

# - Ask the user to input their name and age, then store them in the dictionary.

# - Add a list of scores (e.g., [70, 85, 90]) to the dictionary.

# - Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".

# - Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".

# - Print out the complete record in this format:

# ```
# Student Record:
# Name: John
# Age: 16
# Scores: [70, 85, 90]
# Passed: True
# Teenager: True
# ```




# student = {}
# s_name = input("What is your name?: ")
# s_age = int(input("How old are you?: "))
# scores = [45, 90, 65, 55, 32]
# score = 0
# score+=scores[0]
# score+=scores[1]
# score+=scores[2]
# score+=scores[3]
# score+=scores[4]
# score/=5
# average_score = (score >= 50)
# s_passed= (average_score)
# age_check = (s_age >=13) and (s_age <= 19)
# student = dict(name=s_name, age=s_age, passed=s_passed)
# print(f"Student Record: \nName: \t\t{s_name}\nAge: \t\t{s_age}\nScores: \t{scores}\npassed: \t{s_passed}\nTeenager:\t{age_check}") 


# **Task5: Store Inventory Update**
# - Create a dictionary called store with items and their available quantities. Example:
# ```
# store = {"Book": 10, "Pen": 20, "Bag": 5}
# ```


# - Ask the user to input the item they want to buy (e.g., "Pen").

# - Ask the user to input the quantity they want to purchase.

# - Use the assignment operator -= to update (reduce) the item quantity in the dictionary.

# - Print the updated dictionary in this format:

# ```
# Before purchase: {'Book': 10, 'Pen': 20, 'Bag': 5}
# After purchase: {'Book': 10, 'Pen': 18, 'Bag': 5}
# ```

store = {"50cl pet coke": 175, "50cl pet fanta": 50, "5ocl pet sprite": 100, "Predator": 70, "85cl pulpy orange": 500, "78cl berry blast": 50}
print("Before purchase: ", store)
product = input("What do you want to buy from us?: ")
quantity = int(input("What is the quantity of product you want?: "))
store[product] -= quantity
print("After purchase: ", store)


# **Task6**

# - The Federal Government of Nigeria has set the minimum age for admission into federal tertiary institutions at 16 years old for the 2025/2026 academic session, according to the Minister of Education, Dr. Tunji Alausa. This policy, announced at the 2025 JAMB policy meeting, replaces the previous 18-year minimum age requirement. 

# - For the 2025/2026 academic session, the University of Lagos (UNILAG) requires candidates to have a minimum UTME score of 200 to be eligible for the Post-UTME screening. The Post-UTME itself is an online screening exercise. UNILAG does not release specific departmental cut-off marks before the screening. The departmental cut-off marks are determined after the Post-UTME, based on merit and the performance of candidates in both UTME and the Post-UTME. 

# Breakdown of the Admission Process:
# 1. UTME:
# Candidates must score 200 or above in the UTME and choose UNILAG as their first choice. 
# 2. O'Level Requirements:
# Candidates must also have five (5) credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics. 
# 3. Post-UTME:
# Eligible candidates participate in the university's online Post-UTME screening. 
# 4. Departmental Cut-off Marks:
# After the Post-UTME, the university determines departmental cut-off marks based on merit and overall performance
# (This can range from 200 to 320). 
# 5. Final Admission:
# Candidates who meet the departmental cut-off marks are offered admission. 

# - Write a program to account for all of the conditions above, Such that when a user imputes all their required details, they are told if they will be legible for admission or not.


# Collecting candidate's details.
print("UNILAG Admission Eligibility cher for 2025/2026 session")
print("Fill your details appropriately to check your eligibility for your admission.") 
name = input("What is your name?: ").title()
age = int(input("What is your age?: "))
UTME_score = int(input("What is your UTME score?: "))
Waec_Neco = input("Do you have 5 credit passes at one sitting including English and Mathematics in your o'level result?: Yes or No").title()
post_utme_eligibility = input("Did you participate in the university's online post-UTME screening? Yes or No: ")
post_utme_score = int(input("What is your post utme score?: "))
dept_cutoff = int(input("What is your post utme score: 200-320: "))
eligibility = (age >=16) and (UTME_score>=200) and (Waec_Neco == "Yes") and (post_utme_eligibility =="Yes") and (dept_cutoff >=200 <=320)
if eligibility == True:
    print(f"Dear {name}, Congratulations! You have been offered admission into UNILAG.")
elif eligibility == False:
    print(f"Dear {name}, Sorry! You are not offered admission into UNILAG. Try again next year")
else:
    print("Invalid input, try again later")