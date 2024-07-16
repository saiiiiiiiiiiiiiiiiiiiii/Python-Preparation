# import time

# def timer(func):
#   def wrapper(*args, **kwargs):
#     start = time.time()
#     result = func(*args, **kwargs)
#     end = time.time()
#     print(f"{func.__name__} with the time {end - start}")
#     return result
#   return wrapper

# @timer
# def example_function(n):
#   time.sleep(n)

# example_function(2)



def Debugging(func):
  def wrapper(*args, **kwargs):
    print(f"Calling {func.__name__} with {args} and {kwargs}")
    result = func(*args, **kwargs)
    print(f"Result: {result}")
    return result
  return wrapper


@Debugging
def Example_function(name, greeting="Hello"):
  result = f"{name} {greeting}"
  print(result)
  return result

Example_function("Sainath", greeting="Namaste")