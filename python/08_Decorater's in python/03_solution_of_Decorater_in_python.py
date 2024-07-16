import time

def cache(func):
  def wrapper(*args, **kwargs):
    if args in wrapper.cache:
      return wrapper.cache[args]
    else:
      wrapper.cache[args] = func(*args, **kwargs)
      return wrapper.cache[args]
  wrapper.cache = {}
  print(wrapper.cache)
  return wrapper
  
# def cache(func):
#     cache_value = {}
#     print(cache_value)
#     def wrapper(*args, **kwargs):








@cache
def Long_Running_function(a,b):
  time.sleep(4)
  return a+b



print(Long_Running_function(2,3))
print(Long_Running_function(2,3))
print(Long_Running_function(4,3))