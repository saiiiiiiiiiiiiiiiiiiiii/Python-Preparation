# Learn about Decorater's 

# Problem 1 : Timing Function Execution 
# Write a Decorator that measure's the time a function take's to execute 

# import time

# def timer(func):
#   def wrapper(*args, **kwargs):
#     start = time.time()
#     result = func(*args, **kwargs)
#     end = time.time()
#     print(f"Function {func.__name__} took {end - start} seconds to execute")
#     return result
#   return wrapper


# @timer
# def example_function(n):
#   time.sleep(n)


# example_function(2)




