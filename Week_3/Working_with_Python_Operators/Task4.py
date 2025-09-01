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




student = {}
s_name = input("What is your name?: ")
s_age = int(input("How old are you?: "))
scores = [45, 90, 65, 55, 32]
score = 0
score+=scores[0]
score+=scores[1]
score+=scores[2]
score+=scores[3]
score+=scores[4]
score/=5
average_score = (score >= 50)
s_passed= (average_score)
age_check = (s_age >=13) and (s_age <= 19)
student = dict(name=s_name, age=s_age, passed=s_passed)
print(f"Student Record: \nName: \t\t{s_name}\nAge: \t\t{s_age}\nScores: \t{scores}\npassed: \t{s_passed}\nTeenager:\t{age_check}") 
