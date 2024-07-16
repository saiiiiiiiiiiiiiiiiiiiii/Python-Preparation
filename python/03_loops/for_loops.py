# for loops are used for sequential traversal (travelling)  for travelling through list , tupples , etc 
# vegitables = [ "potato", "tomato","lady Finger", "Brinjal", "Ginger"]
# for element in vegitables:  # applying the for loop on the list []
#   print(element , end=", ")
#  This is the basic example of the list , string tupple 
# list = [ 1,2,3,4,5,6,7,8,9,10] # applying the for loop on the List []
# for element in list:
#   print(element, end=", ")

# tuple = (1,2,3,4,5,6,7,8,9,10) # applying the for loop on tuple ()
# for element in tuple:
#   print(element, end=", " )

# string = "Sainathvilasmore" # applying the for loop on the string
# for element in string:
#   if(element == "v"):
#     print(" v Found")
#     break
#   print(element )
# else:
#   print("End!!!!")

# list = [1,4,9,16,25,36,49,64,81,100]
# for element in list:
#   print(element , end=",")

# Search for number x usin for loop
# list = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter a Number:-  "))
# index = 0
# for element in list:
#   if(element == x):
#     print(f"Number found at index {index}")
#   index = index + 1

# Range function in for loop python range(start value, Ending value , step value)

# for element in range(1 , 6 , 2):
#   print(element)


# Question no 1) Print Number's from 1 to 100
# for element in range(1 , 101):
#   print(element)


# Question 2 ) Print Number from 100 to 1 
# for element in range(100 , 0 , -1):
#   print(element)

# Question no 3) Print the multiplication table of number n 
# n = int(input("Enter a Number:-  "))
# for element in range(1 , 11):
#   print(f"{n} * {element} = {n*element}")


# 
n = int(input("Enter a Number:-  "))
factorial = 1
for element in range(1 , n+1):
  factorial = factorial * element
  print(f"Factorial of {n} is {factorial}")