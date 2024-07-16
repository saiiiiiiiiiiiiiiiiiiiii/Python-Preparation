# 2) Sum of even Numbers 
# Calculate the sum of even numbers up to given number n 

n = int(input("Enter a Number:-  "))
sum = 0
for i in range(1, n + 1):
  if i % 2 == 0:
    sum = sum + 1

print(sum)
