# Bangla Calculator

# Import necessary modules
import math

# Define functions for addition, subtraction, multiplication, and division
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

# Print instructions
print("মুহাম্মাদ নফিজ তানভীর সিহাব ")
print("১. যোগ")
print("২. বিয়োগ")
print("৩. গুণ")
print("৪. ভাগ")

# Continue looping until the user wants to exit
while True:
  # Get the operation from the user
  operation = input("ক্যালকুলেশন করতে কমান্ড করুন (১/২/৩/৪): ")

  # Check if the operation is valid
  if operation in ('1', '2', '3', '4'):
    # Get the first number from the user
    num1 = float(input("প্রথম সংখ্যাটি লিখুন: "))

    # Get the second number from the user
    num2 = float(input("দ্বিতীয় সংখ্যাটি লিখুন: "))

    # Perform the calculation
    if operation == '1':
      print(num1, "+", num2, "=", add(num1, num2))
    elif operation == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))
    elif operation == '3':
      print(num1, "*", num2, "=", multiply(num1, num2))
    elif operation == '4':
      print(num1, "/", num2, "=", divide(num1, num2))

    # Ask the user if they want to continue
    next_calculation = input("গণনা চালিয়ে যেতে চান? (Y/N): ")
    if next_calculation == "N":
      break
  else:
    print("অবৈধ ইনপুট!")

# Print the copyright notice
print("মুহাম্মাদ নফিজ তানভীর সিহাব ")

