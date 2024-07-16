# 1. Creating Dictionaries
# Using curly braces
my_dict = {
  "a":1,
  "b":2,
  "c":3
}
#  Using the dict() constructor to declare a Dictionary 
my_dict_using_dict_constructer = dict(a=1, b=2, c=3)


# 2. Accessing Values
# You can access values by referencing their keys.
# Accessing a value
# Value = my_dict['a']
# print(Value)

# Accessing a value Using get() Method
# value = my_dict.get('b')
# print(value)

# value = my_dict.get("d" , "NotFound")
# print(value) ## Output: 'Not Found' (provides a default value if the key doesn't exist)

# 3. Adding and Updating Elements in Dictionary 
# Add or update key-value pairs by assigning values to keys.
# Adding a new key-value pair
my_dict["d"]= 4
# print(my_dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Updating an existing key-value pair in Dictionary 
my_dict["a"] = 10
# print(my_dict) # {'a': 10, 'b': 2, 'c': 3, 'd': 4}


# Using the update() method to update the Dictionary 
my_dict.update({'e':5,'f':6})
# print(my_dict)


# 4. Removing Elements from the Dictionary 
# Remove key-value pairs using del, pop(), or popitem().
# Using del
# del my_dict['b']
# print(my_dict) # {'a': 10, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Using pop()
# value = my_dict.pop('c') # value = 3, {'a': 10, 'd': 4, 'e': 5, 'f': 6}
# print(value)


# Using popitem() (removes and returns the last key-value pair)
# Key_value_pair = my_dict.popitem()
# print(Key_value_pair) # ('f', 6)
# print(my_dict)

# Using clear() (removes all key-value pairs)
# my_dict.clear()
# print(my_dict) # {}


# 5. Checking for Keys
# You can check if a key exists in a dictionary using the in keyword.
exists = "a" in my_dict
# print(exists) # True
exists = "g" in my_dict
# print(exists) # False


# 6. Iterating Over Dictionaries
# You can iterate over keys, values, or key-value pairs.
# Iterating over keys
# for key in my_dict.keys():
    # print(key, end=", ") # Output: a, b, c, d, e, f

# Iterating over values
# for value in my_dict.values():
      # print(value, end=", ") # Output: 10, 2, 3, 4, 5, 6, 

# Iterating over key-value pairs
  # for key, value in my_dict.items(): 
      # print(key, value) # Output: ('a', 1), ('b', 2), ('c', 3)

# 7. Dictionary Methods
# Here are some commonly used dictionary methods:
# 1. dict.clear()
# Removes all items from the dictionary.
# Example:
# d = {'a': 1, 'b': 2, 'c': 3}
# d.clear()
# print(d)

# 2. dict.copy()
# Returns a shallow copy of the dictionary.
# Example
# 0
# d_copy = d.copy()
# print(d_copy) # {'a': 1, 'b': 2, 'c':3}
# d_copy['d'] = 4
# print(d_copy)
# print(d)


# 3. dict.fromkeys(seq[, value])
# Creates a new dictionary with keys from seq and values set to value (defaults to None).
# Example:
# d = {'a': 1, 'b': 2, 'c': 3}
c ={}
# d_keys = dict.fromkeys(d, 0)
# print(d_keys)
# print(d.fromkeys(d))
# print(dict.fromkeys(c))


# 4. dict.get(key[, default])
# Returns the value for key if key is in the dictionary, else default.
# Example:
# d = {'a': 1, 'b': 2, 'c': 3}
# print(d.get('a'))  # Output: 1
# print(d.get('f',0)) # Output: 0

# 5. dict.items()
# Returns a view object that displays a list of dictionary's key-value tuple pairs.
# Example:
d = {'a': 1, 'b': 2, 'c': 3}
# print(d.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])


# 6. dict.keys()
# Returns a view object that displays a list of all the keys in the dictionary.
# Example:
d = {'a': 1, 'b': 2, 'c': 3}
# print(d.keys()) # Output: dict_keys(['a', 'b', 'c'])

# 7. dict.pop(key[, default])
# Removes the specified key and returns the corresponding value. If the key is not found, default is returned if provided, otherwise KeyError is raised.

# Example:
# d = {'a': 1, 'b': 2, 'c': 3}
# print(d.pop('b')) # Output: 2
# print(d) # Output: {'a': 1, 'c': 3}


# 8. dict.popitem()
# Removes and returns a (key, value) pair from the dictionary. Pairs are returned in LIFO (last-in, first-out) order
# Example
d = {'a': 1, 'b': 2, 'c': 3}
# print(d.popitem())
# print(d)


# 9. dict.setdefault(key[, default])
# Returns the value of key if it is in the dictionary; if not, inserts key with a value of default and returns default.
# Example:
d = {'a': 1, 'b': 2}
# print(d.setdefault('a',0)) # Output: 1
# print(d.setdefault('b',0)) # Output: 2
# print(d.setdefault('c',0)) # Output: 0
# print(d) # Output: {'a': 1, 'b': 2, 'c': 0}



# 10. dict.update([other])
# Updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs.
# Example:
d = {'a': 1, 'b': 2}
d.update({'b':"two", 'c':3,'d':4})
# print(d)

# 11. dict.values()
# Returns a view object that displays a list of all the values in the dictionary.
# Example:
d = {'a': 1, 'b': 2, 'c': 3}
# print(d.values()) # Output: dict_values([1, 2, 3])

# 8. Dictionary Comprehensions
# Python also supports dictionary comprehensions, which provide a concise way to create dictionaries.

# Example:
squared = {x:x**2  for x in range(11)}
# print(squared)

# 9. Nesting Dictionaries
# Dictionaries can contain other dictionaries, which is useful for representing complex data structures.
  # nested_dict = {
  #     'person1': {'name': 'John', 'age': 30},
  #     'person2': {'name': 'Jane', 'age': 25}
  # }
# print(nested_dict['person1']['age'])








    
