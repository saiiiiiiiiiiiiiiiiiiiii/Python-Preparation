# 7) Validating Input 
# keep asking the user for input until the enter a number between 1 to 10


while True:
  number = int(input("Enter a Number:-  "))
  if number < 10 and number > 0:
    print("valid Number")
    break