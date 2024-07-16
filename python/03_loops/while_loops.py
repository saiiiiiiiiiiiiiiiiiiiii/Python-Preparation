# Question no 1) print number's from 1 to 100
# i = 1
# while i <= 100:
#   print(f"Hello World {i}")
#   i = i + 1



# Question no 2) print the number's from  100 to 1
# i = 200
# while i >= 1:
#   print(i)
#   i = i - 1

# Question no 3 ) print the multiplication table of number n
# var = int(input("Enter a number :-  "))
# i = 1
# while i <= 10:
#   print(F"{var} * {i} = {var * i}")
#   i = i + 1


#  question no 4 )Print the element's of a list using loop
# nums = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(nums):
#   print(nums[i], end=", ")
#   i = i + 1


# Question no 5 ) Search for the number x in the tupple
# nums = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter a Number:-   "))
# index = 0
# while index < len(nums):
#   if x == nums[index]:
#     print(f"The Number {x} found at index value {index} of the list ")
#   index = index + 1




# break and continue in loops 

# i = 1
# while i <= 10:
#   if i == 5:
#     break
#   print(i)
#   i = i + 1


# i = 100 
# while i >= 1:
#   if i == 50:
#     break
#   print(i)
#   i = i - 1


# continue
# i = 1
# while i <= 10:
#   if i == 5:
#     i = i + 1
#     continue
#   print(i)
#   i = i + 1

# i = 200
# while i >= 1:
#   if i == 100:
#     i = i - 1
#     continue
#   print(i)
#   i = i - 1


# Question no 6) Write a program to find the sum of  first natural numbers .(using while loop)
# i = 1
# sum = 0
# while i <= 5:
#   sum = sum + i
#   i = i + 1
# print(f" the total sum of natural number is {sum}")

# n = int(input("Enter a Number:- "))
# i = 1
# fact = 1
# while i <= n:
#   fact = fact * i
#   i = i + 1
# print(f" the total fact of natural number is {fact}")

# 1. Print Numbers from 1 to 10
# i = 1
# while i <= 10:
#   print(i)
#   i = i + 1

# 2. Sum of First 10 Natural Numbers
# i = 1
# sum = 0
# while i <= 10:
#   sum = sum + i
#   i = i + 1
# print(sum)


# n = int(input("Entera a Number:-  "))
# factorial = 1
# i = 1
# while i <= n:
#   factorial = factorial * i
#   i = i + 1
# print(factorial)


variable = 5
i = 1
while i <= 10:
  print(f"{variable * i}")
  i = i + 1