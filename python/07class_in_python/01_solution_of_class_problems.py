# 1) Basic class and object 
# create a car class with attributes like brand and model Then create an instance of the class 
class Car:
  def __init__(self, brand,model):
    self.brand = brand  # This is attribute 
    self.model = model  # This is attribute

my_First_car = Car("TATA","Safari")  # This is instance 1
print(my_First_car.brand)
print(my_First_car.model)

my_second_car = Car("Toyota","Innova")  # This is instance 2
print(my_second_car.brand)
print(my_second_car.model)