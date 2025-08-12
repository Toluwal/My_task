# define variables with string
name = "Olayemi Oladapo"

# define variables with integer
X =[ 1, 2, 3, 4, 5]

# define variables with float
Y = [ 0.2, 0.8, 1.2, 1.6, 2.0]

print(name)
print(X)
print(Y)

# int()
# float()
# str()
# bool()

# convert input to integer 
age = int(input("Enter your age: "))
print(f"You will be {age + 1} years old next year.")

# Calculator using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")

# Buy data plan

buy_data = int(input("Enter your code: "))
print(f" 1.Daily \n 2.2-3 days \n 3.Weekly \n 4.Momthly \n 5.2months+ \n 6.Social Bundles \n 7.Broadband \n 8.Binge Bundles \n 9.Family Share \n 10.Hot Deals \n 99.Next \n 0.Back")
