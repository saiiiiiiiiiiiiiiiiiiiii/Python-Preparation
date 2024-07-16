# 2) Class Method and Self
# Add a Method to the Car Class That displays the full name of the car
class Car:
  def __init__(self, brand,model):
    self.brand = brand  # This is attribute 
    self.model = model  # This is attribute

  def full_Name(self):
    return f"{self.brand} {self.model}"

my_First_car = Car("TATA","Safari")  # This is instance 1
print(my_First_car.brand)
print(my_First_car.model)
print(my_First_car.full_Name())

my_second_car = Car("Toyota","Innova")  # This is instance 2
print(my_second_car.brand)
print(my_second_car.model)