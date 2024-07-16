# 5) find the first non repeated character 
# Given a string , find the first non-repeated character 

string = input("Enter you're Name:- ")
for char in string:
  if string.count(char) == 1:
    print(char)
    break