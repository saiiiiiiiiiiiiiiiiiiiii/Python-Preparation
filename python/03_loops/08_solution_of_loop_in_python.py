# 8) Prime Number checker 
# check if a number is prime or not 
number = int(input("Enter a Number:-  "))
isPrime = True
if number   > 1:
  for i in range(2, number):
    if number % i == 0:
      isPrime = False
      break
print(isPrime)
