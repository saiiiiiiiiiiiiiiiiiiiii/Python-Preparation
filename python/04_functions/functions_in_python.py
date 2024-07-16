# Learn all about function's by answering them 

# Basic functions syntax 
# def square(n):
#   return n * n
# print(square(4))



# 2) function with multiple parameter's 
# Create a function that takes two number's as a parameter's and return's their sum
# def sum_of_numbers_(a,b):
#   return a + b

# result = sum_of_numbers_(2,3)
# print(result)


# 3) Polymorphism in Function's 
# Write a Function multiply that multiplies two number's ,but can also accept and multiply string's
# def multiply(a,b):
#   return a * b 
# print(multiply(2,3))
# print(multiply("Sainath",5))

# 4)Function Returning Multiple values
# Create a Function that return's both the area and circumfrence of a circle given its radius 
# def area_circumfrence(radius):
#   area = 3.14 * radius * radius
#   circumfrence = 2 * 3.14 * radius
#   return area,circumfrence
# area,circumfrence = area_circumfrence(5)
# print(area)
# print(circumfrence)

# 5)Default parameter value 
# Write a function that greets a user if no name is provided it should greet with a default name 
# def greet(name="Sainath"):
#   return("Hello " + name)

# print(greet())


# 6)Create a lambda Function to compute a cube of a number .
# cube = lambda x : x * x * x 
# print(cube(2))
# print(cube(4))

# 7) Function with args
# Write a function that takes variable  number of argument's and returns their sum  
# def sum_of_numbers(*args):
#     print(args)
#     for i in args:
#         print(i * 2)
#     return sum (args)
# print(sum_of_numbers(1,2,3,4,5,6,7,8))


# 8)Function with **kwargs
# Create a function that accepts any number of keyword arguments and prints them in the format 
# "key: value"
# def print_key_value(**kwargs):
#   for key, value in kwargs.items():
#     print(f"{key}:{value}")
# print_key_value(name="Sainath",age=20,city="Thane",height= 5.9)


# 9) Generator function with yeild 
# write a generatoe function that yeilds even number's up to a specified limit
# def even_numbers(limit):
#   for i in range(limit):
#       if i % 2 == 0:
#         yield i
# print(even_numbers(10))
# for i in even_numbers(10):
#     print(i)


# Recursive Function
# Create a recursive function to calculate a factrial of a number
# def factorial(n):
#   if n == 1:
#     return n
#   else:
#     return n * factorial(n-1)
# print(factorial(5))


# number = int(input("Enter a Numner:-   "))
# factorial = 1
# for i in range(1, number + 1):
#   factorial = factorial * i

# print(factorial)

# def sum_all(*args):
#   print(args)
#   for i in args:
#     print(i * 2)
#   return sum(args)


# print(sum_all(1,2,3))


# def accept_number(**kwargs):
#   for key,value in kwargs.items():
#     print(f"{key}:{value}")
  
# accept_number(name="Sainath",age=20,city="Thane",height=5.9)


# def print_kwargs(name , power):
#   return(f"Name :{name} power: {power}")


# # print(print_kwargs("Sainath","Confidenece"))
# print(print_kwargs("Sainath","Attitude","Stupid "))



# def even_generator(Limit):
#   for i in range(1, Limit + 1):
#     if i % 2 == 0:
#      yield i
  
# for num in even_generator(10):
#     print(num)


# def factorial(n):
#   if n == 0 or n == 1:
#     return 1
#   else:
#     return n * factorial(n - 1)
  
# print(factorial(5))


# def square(n):
#   return n * n

# print(square(2))



# def sum_of_two_num(num1 , num2):
#   return num1 + num2

# print(sum_of_two_num(2,3))
  


# def multiply(a , b):
#   return a * b

# print(multiply(2,3))
# print(multiply(2,"sai"))
# print(multiply("sai",2))

# def area_of_circle_and_Circumference(radius):
#   Area = 3.14 * radius * radius 
#   circumference = 2 * 3.14 * radius
#   return Area , circumference
# a , c = area_of_circle_and_Circumference(5)
# print(a)
# print(c)

# def Default_name(name="Sai"):
#   return "Hello  " + name

# print(Default_name("Sainath"))
# print(Default_name())

# cube = lambda a : a*a*a
# print(cube(2))

# def sum_all(*args):
#   return sum(args)

# print(sum_all(1,2,3,4,5,6,7,8,9,10))

# def keyWord_argument(**kwargs):
#   for key, value in kwargs.items():
#     return(key, value)

# print(keyWord_argument(Name = "Sainath",Age = 21,))


# def even_generator(limit):
#   for i in range(1,limit+1):
#     if i % 2 == 0:
#       yield i
      

# for num in even_generator(10):
#   print(num)

# def factorial(n):
#   if n == 0 or n == 1:
#     return 1
#   else:
#     return n * factorial(n - 1)
  
# print(factorial(5))