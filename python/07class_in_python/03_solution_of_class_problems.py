# 3) Inheritence
# Create an Electric Class that inherits from the Car Class and has an additional attribute 
class Car:
  def __init__(self, brand,model):
    self.brand = brand  # This is attribute 
    self.model = model  # This is attribute

  def full_Name(self):
    return f"{self.brand} {self.model}"
  
class ElectricCar(Car):
  def __init__(self, brand, model, battery):
    super().__init__(brand, model)
    self.battery = battery

my_First_Electric_car = ElectricCar("Tesla","Model S","85KWH")
print(my_First_Electric_car.full_Name())
print(my_First_Electric_car.brand)
print(my_First_Electric_car.model)
print(my_First_Electric_car.battery)

# my_First_car = Car("TATA","Safari")  # This is instance 1
# print(my_First_car.brand)
# print(my_First_car.model)
# print(my_First_car.full_Name())

# my_second_car = Car("Toyota","Innova")  # This is instance 2
# print(my_second_car.brand)
# print(my_second_car.model)