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