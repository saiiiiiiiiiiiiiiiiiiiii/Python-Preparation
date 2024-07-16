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