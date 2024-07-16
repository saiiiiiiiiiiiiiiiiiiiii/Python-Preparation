# username = "chaiaurcode"

# def func1():
#   # username = "Chai"
#   print(username)


# print(username)
# func1()

x = 99
# def func2(y):
#   z = x + y
#   return z

# result = func2(1)
# print(result) 

# def func3():
#   global x
#   x = 12
  
  
# func3()
# print(x)


# def f1():  # This Example is closure 
#   x = 88
#   def f2():
#     print(x)
#   return f2
# myresult = f1()
# myresult()


def chaicoder(num):
  def actual(x):
    return x ** num
  return actual

f = chaicoder(2)
print(f(2))

