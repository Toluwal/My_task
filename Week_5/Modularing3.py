###  Modularizing Your Codes 3 (Object Oriented Programming)

### Table of Contents

# 1. Introduction to Classes
# 2. Why Classes are Important
# 3. Basic Class Structure
# 4. Objects and Instances
# 5. The __init__ Method
# 6. Understanding `self`
# 7. Attributes
# 8. Methods
# 9. Other Important Methods
# 10. Simple Examples
# 11. Intermediate Examples
# 12. Complex Examples
# 13. Best Practices

# **What is a Class?**

# A class is like a blueprint or template that defines what something should look like and what it can do. Think of it as a meat pie cutter - it defines the shape and characteristics, but it's not the actual meat pie itself.

# - Take a look at this;

#  - A house blueprint shows where rooms go, but it's not a house you can live in.
#  - A car design document describes features, but you can't drive the design.
#  - A recipe tells you how to make a cake, but the recipe is not edible.

# **Object/Instance**

# **What is an Object/Instance?**

# An object (also called an instance) is a specific, real item created from a class blueprint. It's the actual "thing" you can use and interact with.

# - Take a look at this;
#   - Your actual house built from the blueprint.
#   - A specific Toyota Camry manufactured from car designs.
#   - The delicious cake baked from the recipe.

### Key Characteristics of Classes

# - Encapsulation: Groups related data and functions together
# - Abstraction: Hides complex implementation details
# - Inheritance: Can create new classes based on existing ones (Reusability -Write once, use many times)

### Why Classes are Important

# - Classes help us:

#    - Organize Code: Keep related data and functions together
#    - Model Real World: Represent real-world entities in code
#    - Reduce Repetition: Avoid writing the same code multiple times
#    - Maintain Code: Easier to update and fix bugs
#    - Scale Applications: Build larger, more complex programs

# The Foundation
# -  `__init__` and `self`

#    - Before we dive into attributes and methods, we need to understand two special concepts that make everything work: __init__ and self.

# What is init ?

# `__init__` is a special method (called a constructor) that automatically runs when you create a new object. Think of it as the "birth certificate" process - it sets up all the basic information about the new object.

# **Real-World Analogy**

# - When a baby is born in Nigeria, certain things happen automatically:

#    - Birth certificate is created
#    - Name is assigned
#    - Parents are recorded
# -  - Date of birth is noted

# - Similarly, when an object is "born" (created), `__init__` automatically:

#    - Sets up the object's attributes
#    - Assigns initial values
#    - Prepares the object for use

# class Student:
#     def __init__(self, name, course, level):  # This runs automatically.
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been created!")

# When you create a student, __init__ runs automatically
# kemi = Student("Kemi Adebayo", "Computer Science", 300)
# print(kemi.name)

# **What is self ?**
# `self` is a reference to the specific object you're working with. It's like saying "this particular student" or "this specific bank account."

# **Real-World Analogy**
# - In a classroom with many students:
 
#    - When the teacher says "Kemi, what is your course?" - "your" refers to Kemi specifically
#    - When the teacher says "Chinedu, what is your level?" - "your" refers to Chinedu specifically

# - In programming:

#    - self.name means "this specific object's name"
#    - self.course means "this specific object's course"

# **Visual Illustration**
# ```
# Class: Student (The Template)
# ├── def __init__(self, name, course):
# │   ├── self.name = name      ← "Give THIS object a name"
# │   └── self.course = course  ← "Give THIS object a course"

# Creating Objects:
# ├── kemi = Student("Kemi", "CS")
# │   └── self refers to kemi → kemi.name = "Kemi"
# ├── chinedu = Student("Chinedu", "Engineering") 
# │   └── self refers to chinedu → chinedu.name = "Chinedu"
# └── fatima = Student("Fatima", "Medicine")
#     └── self refers to fatima → fatima.name = "Fatima"

# ```

# How init and self Work Together

# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: Create student object...")
#         self.name = name    # Step 2 Assign name to THIS object
#         self.state_of_origin = state  # Step 2: Assign name to THIS object
#         self.course = course   # Step 3: Assign state to THIS object
#         self.student_id = self.generate_id()  # Step 5: Generate ID for THIS object
#         print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")
#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000, 9999)}"

# When you create an object, here's what happens:
# ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")
# print(ayo.name)
# print(ayo.student_id)
# print(ayo.course)

# More example:
class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network}")

    def buy_airtime(self, amount):
        self.airtime += amount   # self ensures it goes to the RIGHT person
        return f"{self.name} now has ₦{self.airtime} airtime"
    
# Creating multiple users
abeeb = PhoneUser("Abeeb Bakare", "MTN")
onisemo = PhoneUser("Onisemo Williams", "Airtel")
# Each person's actions affect only their own account
print(abeeb.buy_airtime(500))   # Abeeb Bakare now has ₦500 airtime
print(onisemo.buy_airtime(1000))   # Onisemo Williams now has ₦1000 airtime
print(abeeb.airtime)  # 500
print(onisemo.airtime) # 1000
        
# **Key Rules**

# 1. __init__ always takes self as first parameter
# 2. All methods take self as first parameter
# 3. Never pass self manually when calling methods
# 4. Use self inside methods to access object's attributes
# 5. self refers to the specific object being used

### Attributes

# **What are Attributes?**
# Attributes are the characteristics, properties, or data that describe an object. They answer the question "What does this object look like?" or "What information does this object store?"

# **Real-World Analogy**

# - Think of a Nigerian National ID card

#     - me: "Adebayo Tosin"
#     - Age: 28
#     - State of Origin: "Lagos"
#     - LGA: "Ikeja"
#     - Occupation: "Software Developer"

# - These are all attributes - they describe WHO the person is, not what they can DO.

# Defining Attributes of a student
class Student:
    def __init__(self, name, course, level, state_of_origin):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = 0.0

    def get(self, cumulative):
        self.cgpa += cumulative   # self ensures it goes to the RIGHT person
        return f"{self.name} has {self.cgpa} CGPA"
    
# Creating a student object
Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State")

# Acessing attributes
print(Fathia.name)
print(Fathia.course)
print(Fathia.state_of_origin)
print(Fathia.get(4.75))

# Types of Attributes

# 1. Instance Attributes - Unique to each object

student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

print(student1.name)
print(student2.name)

# Class Attributes - Shared by all objects of the class

class Student:
    university = "Federal University of Technology Akure"  
    
    def __init__(self, name, course, level, state_of_origin):
        self.name = name         
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin

    def get_university(cls):
        return cls.university

student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

print(Student.university)     
print(student1.university)   
print(student2.university)    

# # Methods: The Actions (What Objects CAN DO)
# **What are Methods?**

# Methods are functions that belong to a class. They define what actions an object can perform. They answer the question "What can this object do?"

# **Real-World Analogy**
#  - Think of what a Nigerian student can do

#     - Study()
#     - WriteExam()
#     - PaySchoolFees()
#     - RegisterCourses()
#     - AttendLectures()

# These are all methods - they describe what the person can DO, not what they look like.

class Student:
    def __init__(self, name, course, level):
        # Attributes
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False
     # Method: action the student can do
    def pay_School_fees(self):
        self.fees_paid = True
        return f"{self.name} has paid school fees for {self.level} level"
     # Method: another action
    def register_courses(self):
        if self.fees_paid:
            return f"{self.name} has registered courses for {self.course}"
        else:
            return f"{self.name} must pay school fees first!"
     # Method: calculate_cgpa(self, grades):
    def calculate_cgpa(self, grades):
        if grades:
            self.cgpa = sum(grades) / len(grades)
            return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
        return "No grades provided"
    
    # Using methods
Abiodun = Student("Abiodun Akinola", "Gistology", 600)
print(Abiodun.pay_School_fees())        
print(Abiodun.register_courses())       
print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))
    

 # Types of Methods  
 # 1. Instance Methods - Work with specific object data

 # 'self' refers to the specific student
def pay_School_fees(self):
    return f"{self.name} has paid school fees"

 # 2. Class Methods - Work with class-level data

@classmethod

def get_university(cls):
    return cls.university

 # 3. Static Methods - Don't need object or class data

def academic_calendar():
    return "Academic session run from September to July"

# **How Attributes and Methods Work Together**

# - The Relationship

#   - Attributes store the data
#   - Methods use and modify that data


class BankAccount:
    def __init__(self, owner, bank_name, balance=0):
        # ATTRIBUTES - What the account HAS
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()

    # METHODS - What the account can DO
    def deposit (self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount    # Method changes attribute
            return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount   # Method changes attribute
            return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,} "
        return("Indufficient funds or invalid amount")
    
    def trasfer(self, amount, recipient):
        """Transfer money to another account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
        return "Trensfer failed: Insufficient funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
    def generate_account_number(self):
        """Generate a unique account number"""
        import random
        return f"01{random.randint(10000000, 99999999)}"
    
    # Creating and using the account

    adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 50000)

    # Attributes (characteristics)
    print(f"owner: {adunni_account.owner}")
    print(f"Bank: {adunni_account.bank_name}")
    print(f"Account Number: {adunni_account.account_number}")

    # Methods (actions)
    print(adunni_account.deposit(25000))
    print(adunni_account.withdraw(10000))
    print(adunni_account.transfer(15000, "Sunday James"))
    print(adunni_account.check_balance())

#     **Visual Representation**
# ```

# CLASS: Danfo Bus
# ├── ATTRIBUTES (What it HAS)
# │   ├── route = "Garage to Ogolonto"
# │   ├── conductor_name = "Juwon"
# │   ├── capacity = 4
# │   ├── current_passengers = 0
# │   └── fare = 200
# │
# └── METHODS (What it can DO)
#     ├── pick_passenger() → current_passengers increases
#     ├── drop_passenger() → current_passengers decreases
#     ├── collect_fare() → "Pay your ₦200!"
#     ├── announce_bus_stop() → "Next stop: Ebute!"
#     └── honk() → "Pam pam pam!"

# OBJECT: my_danfo
# ├── Uses the attributes with specific values
# └── Can perform all the methods
# ```

## Attributes vs Methods 

# | **Attributes** | **Methods** |
# |----------------|-------------|
# | Store data/information | Perform actions |
# | Answer "What is it?" | Answer "What can it do?" |
# | Nouns (name, course, state) | Verbs (study, pay, register) |
# | Hold values | Execute code |
# | Can be read/changed | Can be called/executed |
# | `student.name` | `student.pay_fees()` |


# Practice Exercise1

class NaijaPhone:
    def __init__(self, brand, model, network_provider):
        self.brand = brand
        self.model = model
        self.network_provider = network_provider
        self.airtime_balance = 0
        self.data_balance = 0
        self.is_on = False
    
    def power_on(self):
        self.is_on = True
        return f"{self.brand} phone is now on. Network: {self.network_provider}"
    
    def buy_airtime(self, amount):
        self.airtime_balance += amount
        return f" ₦{amount} airtime purchased. Balance: ₦{self.airtime_balance}"
    
    def make_call(self,message, number):
        if self.is_on and self.airtime_balance > 0:
            self.airtime_balance -= 10
            return f"Calling {number}... Remaining airtime: ₦{self.airtime_balance}"
        return "Cannot make call. Check your pghone power and airtime balance"
    
    def send_sms(self, message, number):
            if self.airtime_balance >= 4:
                self.airtime_balance -= 4
                return f"SMS sent to {number}: '{message}'. Remaining airtime: ₦{self.airtime_balance}"
            return "Insufficient airtime to send SMS"


# Practice Exercise2

# Given this class, identify the attributes and methods

class BRTBus:
    def __init__(self, route, bus_number):

        self.route = route
        self.bus_number = bus_number
        self.current_stop = "Ikorodu"
        self.passenger_count = 0
        self.fare = 300

    def announce_stop(self):
        return f"Next stop: {self.current_stop} Fare is ₦{self.fare}"
    
    def board_passengers(self, count):
        self.passenger_count += count
        return f"{count} passengers boarded. Total: {self.passenger_count}"
    

# Practice Exercise3

# Given this class, identify the attributes and methods

class MarketTrader:
    def __init__(self, name, market_name, goods):

        self.name = name
        self.market_name = market_name
        self.goods = goods
        self.daily_sales = 0

    def advertise_goods(self):
        return f"{self.name} at {self.market_name}: Fresh {','.join(self.goods)} available!"
    
    def make_sale(self, amount):
        self.daily_sales += amount
        return f"Sale made! Today's total: ₦{self.daily_sales:,}"
    
#     **What is Encapsulation?**

# Encapsulation is like putting related items in a box and controlling who can access them. It groups related data (attributes) and functions (methods) together in one class, and controls how they can be accessed from outside.

# - Real-World Analogy - Think of an ATM machine:

#    - Inside the ATM: Cash, card reader, computer system, cameras
#    - What you can access: Keypad, screen, card slot, cash dispenser
#    - What you cannot access: Internal cash storage, computer motherboard, security cameras

# - The ATM encapsulates all its internal components and only gives you safe ways to interact with it.
    
class NigerianBankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance   # Protected attribute
        self.pin = "1234"   # Private attribute
        self._transaction_history = []     # Protected attribute

    # Public methods - anyone can use these
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transaction_history.append(f"Deposited ₦{amount:,}")
            return f"₦{amount:,} deposited successfully"
        return "Invalid deposit amount"
    
    def withdraw(self, amount, pin):
        if self.__verify_pin(pin):   # Uses private method
            if amount <= self.balance:
                self._balance -= amount
                self._transaction_history.append(f"Withdrew ₦{amount:,}")
                return f"₦{amount:,} withdrawn successfully"
            return "Insufficient funds"
        return "Invalid pin"
    
    def check_balance(self, pin):
        if self.__verify_pin(pin):
            return f"Current balance: ₦{self._balance:,}"
        return "Invalid PIN"
    
    # Private method - only the class can use this

    def __verify_pin(self, entered_pin):
        return (entered_pin == self.__pin)
    
    # Protected method - subclasses can use this
    def _get_transaction_history(self):
        return self._transaction_history.copy()
    

    # Using the encapsulated account
ibrahim_account = NigerianBankAccount("Ibrahim Orekunrin", 50000)

# These work - public interface
print(ibrahim_account.deposit(10000))      # ₦10,000 deposited successfully
print(ibrahim_account.withdraw(5000, "1234"))  # ₦5,000 withdrawn successfully
print(ibrahim_account.check_balance("1234"))   # Current balance: ₦55,000
    


# Try this out...
# But it won't work - private/protected data

print(ibrahim_account.__pin)          # Error! Cannot access private attribute
ibrahim_account.__verify_pin("1234")  # Error! Cannot access private method

# **Benefits of Encapsulation**

# - Security: Sensitive data (like PIN) is protected
# - Organization: Related functions stay together
# - Control: You decide how data can be accessed
# - Maintenance: Changes inside don't break outside code

# ```python
# class Example:
#     def __init__(self):
#         self.public = "Anyone can access"           # Public
#         self._protected = "Subclasses can access"   # Protected (convention)
#         self.__private = "Only this class can access"  # Private (name mangling)

# ```

# Abstraction

# **What is Abstraction?**

# Abstraction means hiding complex implementation details and showing only the essential features. It's like using a remote control - you press buttons to change channels, but you don't need to know how the TV circuits work.

# **Real-World Analogy** 
# - When you board a Lagos Danfo

#    - What you see: Door, seats, conductor, driver
#    - What you use: "Oya enter!" (get in), pay fare, say "Owa!" (stop here)
#    - What you don't see: Engine mechanics, fuel injection, electrical wiring
#    - What you don't need to know: How the engine converts fuel to motion

# - The bus abstracts all the complex mechanical details. You just need to know how to be a passenger.

from abc import ABC, abstractmethod
# Abstract base class - defines what a Nigerian student should do
class NigerianStudent(ABC):
    def __init__(self, name, course, level):
        self.name = name
        self.course = course
        self.level = level
        self.fees_paid = False

    # Concrete method - all students can do this
    def pay_school_fees(self, amount):
        self.fees_paid = True
        return f"{self.name} paid {amount:,} school fees"        


    # Abstract method - all students can do this
    def study_method(self):
        pass

    def take_exam(self):
        pass

# Concrete classes - specific implementations

class MedicalStudent(NigerianStudent):
    def study_method(self):
        return f"{self.name} studies anatomy books and practices on cadavers" 
    
    def take_exam(self):
        return f"{self.name} takes practical exam in the anatomy lab"
    
    class EngineeringStudent(NigerianStudent):
        def study_method(self):
            return f"{self.name} solves mathematical problems and builds prototypes"
        
    def take_exam(self):
        return f"{self.name} takes exam with calculations and technical drawings"
    
    class ComputerScienceStudent(NigerianStudent):
        def study_method(self):
            return f"{self.name} codes programs and debugs software"
        
    def take_exam(self):
        return f"{self.name} takes practical programming exam on computer"

# Using abstraction
students = [
    MedicalStudent("Dr. Adeyinka Ogunsanya", "Medicine", 400),
    EngineeringStudent("Dr. Ajala Gift", "Mechanical Engineering", 300),
    ComputerScienceStudent("Fatima Hassan", "Computer Science", 200)
]

# Same interface, different implementations
for student in students:
    print(student.pay_school_fees(150000))   # Same for all
    print(student.study_method())    # Different for each
    print(student.take_exam())       # Different for each
    print("---")


    # more example on abstraction

    # Simple abstaction for phone interface

    class SimplePhone:
        def __init__(self, brand):
            self.brand = brand
            self._complex_internal_system = "Very complicated stuff"

    # Simple interface - user doesn't need to know internal complexity
        def make_call(self, number):
            self._establish_network_connection()
            self._encode_voice_signal()
            self._transmit_to_tower()
            return f"Calling {number} from {self.brand} phone..."
            
        def send_sms(self, message, number):
            self._connect_to_sms_center(
            )
            self._format_message()
            self._send_through_network()
            return f"SMS sent to {number}: '{message}'"   
        
        # Complex internal methods - hidden from user
        def _establish_network_connection(self):
            # complex networking code here
            pass

        def _encode_voice_signal(self):
            # Complex audio processing here
            pass

        def _transmit_to_tower(self):
            # Complex radio transmission here
            pass

# User only needs to know the simple interface

my_phone = SimplePhone("Techno")
print(my_phone.make_call("08012345678"))  # Simple to use
print(my_phone.send_sms("How far?", "08098765432"))      # Don't need to know internals

# **Benefits of Abstraction**

# - Simplicity: Complex systems become easy to use
# - Focus: Users focus on what matters, not how it works
# - Flexibility: Implementation can change without affecting users
# - Reusability: Same interface works for different implementations

### Inheritance - Building on What Already Exists

# **What is Inheritance?**

# Inheritance allows you to create new classes based on existing ones. The new class (child) inherits attributes and methods from the parent class, and can add its own features or modify existing ones.

# - Real-World Analogy
#    - Think of a Nigerian family

#        - Parent (Father): Adebayo Ogundimu - has surname, family traditions, property
#        - Child 1 (Son): Kemi Ogundimu - inherits surname, traditions, gets family property + adds his own career as doctor
#        - Child 2 (Daughter): Tunde Ogundimu - inherits surname, traditions, gets family property + adds her own career as engineer

# - The children inherit from their father but also have their own unique characteristics.

# Parent class - Base Nigerian Person

class NigerianPerson:
    def __init__(self, first_name, last_name, state_of_origin):
        self.first_name = first_name
        self.last_name = last_name
        self.state_of_origin = state_of_origin
        self.can_speak_english = True

    def introduce(self):
        return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}"
    
    def greet(self):
        return "Good morning!"
    
    def speak_local_language(self):
        return "I speak my local language"
    
    # Child class 1 - Nigerian Student inherits from NigerianPerson

    class NigerianPerson:
        def __init__(self, first_name, last_name, state_of_origin):
            self.first_name = first_name
            self.last_name = last_name
            self.state_of_origin =state_of_origin
            self.can_speak_english = True

        def introduce(self):
            return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}"
        
