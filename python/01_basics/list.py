# # Creating a List
# my_list = [1, 2, 3, 4, 5]
# # print(my_list) # Output: [1, 2, 3, 4, 5]


# # Accessing Elements
# # print(my_list[0]) # Output: 1
# # print(my_list[-1])# Output: 5 (last element)

# # Modifying Elements
# my_list[0] = 1
# # print(my_list)# Output: [10, 2, 3, 4, 5]

# # List Methods
# # append()
# # Adds an element to the end of the list.
# # print(my_list.append(6))
# # print(my_list)

# # extend()
# # extends the list by appending elements from an iterable.
# my_list.extend([7,8,9,10])
# # print(my_list)


# # 3 insert()
# # Inserts an element at a specified position 
# # syxtax goes like my_list.insert(the position which you want to add , and the number you want to add)
# my_list.insert(9,11)
# # print(my_list)

# # 4 remove()
# # Removes the first occurrence of an element.
# my_list.remove(11)
# # print(my_list)

# # 5 pop()
# # Removes and returns the element at the specified position. 
# # If no index is specified, pop() removes and returns the last item.
# my_list.pop()
# # print(my_list)

# # 6 clear()
# # Removes all elements from the list.
# # my_list.clear()
# # print(my_list)


# # 7 index()
# # Returns the index of the first occurrence of an element. 
# # Raises a ValueError if the element is not found.
# # print(my_list.index(3))  # Output: 2

# # 8 count()
# # Returns the number of occurrences of an element in the list.
# # print(my_list.count(3))  # Output: 1


# # 9 sort()
# # Sorts the list in ascending order by default. 
# # You can also pass the reverse=True parameter to sort in descending order.
# my_list.sort(reverse=True)
# # print(my_list)

# # 10 reverse()
# # Reverses the elements of the list in place.
# my_list.reverse()
# print(my_list) # Output : [1, 2, 3, 4, 5, 7, 8, 9]

# # 11 copy()
# # Returns a copy of the list.
# my_list_copy = my_list.copy()
# # print(my_list_copy) # Output : [1, 2, 3, 4
# my_list_copy.append(10)
# # print(my_list_copy) # Output: [1, 2, 3, 4, 5]

# # List Comprehensions
# # List comprehensions provide a concise way to create lists.
# squares = [x**2 for x in range(6)]
# # print(squares)

# # Other Operations
# # Concatenation: You can concatenate lists using the + operator.
# list_1 = [1,2,3,4,5]
# list_2 = [6,7,8,9,10]
# # print(list_1 + list_2)


# # Repetition: You can repeat lists using the * operator.
# repeated_List = list_1 * 2
# # print(repeated_List)


# # Membership Testing: You can check if an element is in a list using the in keyword.
# list_3 = [1,2,3,4,5,6,7,8,9,10]
# # print(3 in list_3)
# # Length: You can get the number of elements in a list using the len() function.
# print(len(list_3))

