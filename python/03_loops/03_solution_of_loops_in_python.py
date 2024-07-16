# 3) Multlipication Table Printer
# print the multiplication table for a given number up to 10 but skip the fifth iteration


for i in range(1, 11):
  for j in range(1, 11):
    if i == 5:
      continue
    print(f"{i} * {j} = {i * j}")