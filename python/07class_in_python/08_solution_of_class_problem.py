# 8) Property Decorator's 
# Use a property decorator in the Car class to make the model attribute read_only 
class Car:
  total_car = 0
  def __init__(self, brand,model):
    self.brand = brand  # This is attribute 
    self.__model = model  # This is attribute
    Car.total_car += 1

  def full_Name(self):
    return f"{self.brand} {self.__model}"
  
  def fuel_type(self):
    return "Petrol or Diesel"
  
  @staticmethod # This is Decorator's in python @ 
  def general_descripition():
    return "Cars are mean's of transport "
  

  @property
  def model(self):
    return self.__model
  
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
# my_First_car.model = "C Class"
# print(my_First_car.brand)
print(my_First_car.model)
# print(my_First_car.full_Name())
# print(my_First_car.fuel_type())
# print(my_First_car.general_descripition())
# print(Car.general_descripition())


# my_second_car = Car("Toyota","Innova")  # This is instance 2
# print(my_second_car.brand)
# print(my_second_car.model)
# print(Car.total_car)