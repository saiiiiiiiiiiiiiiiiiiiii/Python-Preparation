# Creating Strings
# string1 = 'Hello'
# string2 = "Hello"
# string3 = '''Hello'''
# string4 = """Hello"""
# print(string1)
# print(string2)
# print(string3)
# print(string4)

# String Operations
# Concatenation: Joining two or more strings using the + operator.
# str1 = "Hello"
# str2 = " World"
# print(str1 + str2)

# Repetition: Repeating a string using the * operator.

# result = "Hello  " * 3
# print(result)

# 1) Indexing: Accessing individual characters in a string using their index. 
# Python uses zero-based indexing.

# string = "Sainath"
# print(string[0])
# print(string[-1])

# 2) Slicing: Extracting a substring using a slice notation [start:end]. 
# The start index is inclusive, and the end index is exclusive.
# string = "Sainath"
# print(string[0:3]) # Sai

# String Methods
# 1) upper() Method
# 2) Lower() Method
# Python provides many built-in methods to work with strings. Here are some commonly used methods:
# string = "sainath vilas more"
# print(string.upper())
# print(string.lower())

#  3)strip() Method: Remove whitespace from the beginning and end of the string.
# string = "   sainath vilas more   "
# print(string)
# print(string.strip())


# 4) replace() Method : Replace a substring with another substring. 
# string = "Hello World"
# print(string.replace("World",""))
# print(string)

# 5) split(): Split the string into a list / array of substrings based on a delimiter.

# string = "Sainath vilas more"
# print(string.split())

# string =['Sainath', 'vilas', 'more']
# print(", ".join(string))



# String Formatting
# name = "Sainath"
# age = 20
# print(f"my name is {name} and my age is {age}")


# String Immutability
# Since strings are immutable in Python, any operation that modifies a string 
# will actually create a new string.
# string = "Hello"
# new_string = string.replace('H', 'J')
# print(string)      # 'Hello'
# print(new_string)  # 'Jello'


