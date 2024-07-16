# Loop's in python 
# 1) Counting Positive Number's
# Give a List of Number's , count How many are positive 

# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# count = 0
# for number in numbers:
#   if number > 0:
#     count = count + 1
#     print(count)


# 2) Sum of even Numbers 
# Calculate the sum of even numbers up to given number n 

# n = 10 
# sum = 0
# for i in range(1 , n + 1):
#   if i % 2 == 0:
#     sum += 1

# print(sum)
  

# 3) Multlipication Table Printer
# print the multiplication table for a given number up to 10 but skip the fifth iteration

# number = 3
# for i in range(1,11):
#   if i == 5:
#     continue
#   print(f"{number} * {i} = {number * i}")

# for i in range(2,21):
#   for j in range(1, 11):
#     print(f"{i} * {j} = {i*j}")


# 4)  Reverse a string
# Reverse a string using a loop
# string = input("Enter you're name:- ")
# for i in range(len(string) - 1, -1, -1):
#   print(string[i], end = "")
  

# string = input("Enter a string:-  ")
# reverse_String = ""
# for i in string:
#   reverse_String = i + string
# print(reverse_String)


# 5) find the first non repeated character 
# Given a string , find the first non-repeated character 

# string = input("Enter a string:-  ")

# for char in string:
#   print(char)
#   if string.count(char) == 1:
#     print(f"The single character is {char}")
#     break
  


# 6) Factorial Calculator
# compute the factorial of a number using a while loop 
# factorial = 1
# number = int(input("Enter a number:- "))
# if number < 0:
#   print("Sorry, factorial does not exist for negative numbers")
# elif number == 0:
#   print("The factorial of 0 is 1")
# else:
#   for i in range(1, number + 1):
#     factorial = factorial*i
    
#   print("The factorial of", number, "is", factorial)


# number = int(input("Enter a number:-  "))
# factorial = 1
# while number > 0:
#   factorial = factorial * number
#   number -= 1

# print(factorial)

# 7) Validating Input 
# keep asking the user for input until the enter a number between 1 to 10
# while True:
#     number = int(input("Enter a number:-   "))
#     if number > 0 and number <= 10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid Number Please Try again")


# 8) Prime Number checker 
# check if a number is prime or not 
# number = int(input("Enter a Number:-   "))
# is_prime = True
# if number > 1:
#   for i in range(2 , number):
#     if (number % i) == 0:
#       is_prime = False
#       break

#   print(is_prime)



# 9) list Uniqueness checker
# check  if all element's in the list are unique if duplicate is found exit the loop and print the duplicate
# list = [1,2,3,4,5,6,7,8,8,9]
# items = ["apple", "Bananna", "orange", "apple", "mango"]
# for i in items:
#   if items.count(items) == 1:
#     print("All elements are unique")
#   elif items.count(items) != 1:
#     print("Duplicate found")
#     break




# 10) Exponential Backoff
# Implement an Exponential Backoff Stratergy that doubles the waiting time between retries,
# stsrting from 1 sec but stops after 5 retries 
# import time
# waiting_time = 1
# maximum_retries = 5
# attempts = 0
# while attempts < maximum_retries:
#   print(f"attempt's {attempts + 1} waiting time second's  {waiting_time}" )
#   time.sleep(waiting_time)
#   waiting_time *= 2
#   attempts += 1
