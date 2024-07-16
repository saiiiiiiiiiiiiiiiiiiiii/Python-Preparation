# Loop's in Python 
# 1) Counting Positive Number's 
# Given a List of Number's count how many are positive
# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# postive_number_count = 0
# for element in numbers:
#   if element > 0:
#     postive_number_count = postive_number_count + 1
# print(postive_number_count)


# Sum of even number's up to given number n
# n = int(input("Enter a Number "))
# sum = 0
# for element in range(1, n + 1):
#   if element % 2 == 0:
#     sum = sum + element
# print(sum)

# 3) Multiplication Table Printer 
# Print the multiplication table for given number up to 10 but skip the fifth iteration
# number = 3
# for element in range(1 , 11):
#   if element == 5:
#     continue
#   print(f"{number} * {element} = {number * element}")

# 4) Reverse a string
# Reverse a string using loop
# string = input("Give Me a string and i will reverse that :-   ")
# Reverse_string = ""
# for element in string:
#   # print(element,end=", ")
#   Reverse_string = element + Reverse_string 

# print(Reverse_string)


#5) Find the first non -repeated character 
# Given a string find the first nonrepeated character 

# string = input("Enter you're name:-  ")
# non_repeated_character = ""
# for element in string:
#   print(element)
#   if string.count(element) ==  1:
#     non_repeated_character = element
#     break

# print(f"The first non repeated character in the you're name is : {non_repeated_character}")


# 6) factorial of a calculator
# n = int(input("Enter a Number:-  "))
# i = 1 
# factorial = 1
# while i <= n:
#   print(factorial)
#   factorial = factorial * i
#   i = i + 1
# print(f"The factorial of {n} is :- {factorial}")

# n= int(input("enter a number:-  "))
# factorial = 1
# while n > 0:
#   factorial = factorial * n
#   # 1       =     1     * 5 = factorial value will be 5 
#   # 5       =     5     * 4 = factorial value will be 20
#   # 20      =     20    * 3 = factorial value will be 60
#   # 60      =     60    * 2 = factorial value will be 120
#   n = n - 1
# # 5 = 5 - 1 = 4
# # 4 = 4 - 1 = 3
# # 3 = 3 - 1 = 2
# # 2 = 2 - 1 = 1
# print(f"The factorial of {n} is :- {factorial}")

# 7) Validating Input 
# Keep asking the user for input until they enter a number between 1 to 10

# while True:
#   user = int(input("Enter a Number:-  "))
#   if user >=1 and user <=10:
#     print("The number is  in the range of 1 to 10")
#     break
#   else:
#     print("The number is  not in the range of 1 to 10")

# 8) Prime Number checker 
# number = int(input("Enter a Number:-  "))
# prime_number = True
# for element in range(2 , number):
#   if (number % element) == 0:
#     prime_number = False
#     break
# print(prime_number)
 


# items = ["apple", "bananna","orange", "mango", "apple"]
# unique_items = set()
# for element in items:
#   if element in unique_items:
#     print("The item is already in the list" , element)
#     break
#   else:
#     unique_items.add(element)
#     print(unique_items)


# Exponantial Backoff
# implement an exponential backoff stratergy that doubles the wait time 
# between retries strating from 1 second , but stios after 5 retries
import time
wait_time = 1   
max_retries = 5
attempts = 0
while attempts < max_retries:
  print("Attempt",attempts + 1 ,"Wait_time", wait_time)
  time.sleep(wait_time)
  wait_time *= 2
  attempts += 1

