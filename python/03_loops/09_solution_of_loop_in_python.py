# 9) list Uniqueness checker
# check  if all element's in the list are unique if duplicate is found exit the loop and print the duplicate



list = [1,2,3,4,5,6,7,8,8,9]

for items in list:
  # print(items)
  if list.count(items) != 1:
    print("Duplicate")
    print(items)
    break