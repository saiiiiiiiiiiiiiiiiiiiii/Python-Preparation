# 7) Static Method
# Add a static Method to the car Class that return's a general desciription of car 


class Car:
  total_car = 0
  def __init__(self, brand,model):
    self.brand = brand  # This is attribute 
    self.model = model  # This is attribute
    Car.total_car += 1

  def full_Name(self):
    return f"{self.brand} {self.model}"
  
  def fuel_type(self):
    return "Petrol or Diesel"
  
  @staticmethod # This is Decorator's in python @ when we use a keyword "@staticMethod" then we don't need to use the self keyword in the placeholder
  def general_descripition():
    return "Cars are mean's of transport "
  
class ElectricCar(Car):
  def __init__(self, brand, model, battery):
    super().__init__(brand, model)
    self.battery = battery

  def fuel_type(self):
    return "Electric charge"
  



# my_First_car = Car("Tata","Safari")
# print(my_First_car.fuel_type())



# my_First_Electric_car = ElectricCar("Tesla","Model S","85KWH")
# print(my_First_Electric_car.full_Name())
# print(my_First_Electric_car.brand)
# print(my_First_Electric_car.model)
# print(my_First_Electric_car.battery)
# print(my_First_Electric_car.fuel_type())

my_First_car = Car("TATA","Safari")  # This is instance 1
# print(my_First_car.brand)
# print(my_First_car.model)
# print(my_First_car.full_Name())
# print(my_First_car.fuel_type())
print(my_First_car.general_descripition())
# print(Car.general_descripition())


# my_second_car = Car("Toyota","Innova")  # This is instance 2
# print(my_second_car.brand)
# print(my_second_car.model)
# print(Car.total_car)