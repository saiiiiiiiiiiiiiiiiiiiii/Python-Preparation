# Encapsulation
# Modify The Car class to encapsulate the brand attribute making it private and provide a getter method for it
class Car:
  def __init__(self, brand,model):
    self.__brand = brand  # This is attribute 
    self.model = model  # This is attribute

  def full_Name(self):
    return f"{self.__brand} {self.model}"
  
  def get_brand(self):
    return self.__brand + " !"
  
class ElectricCar(Car):
  def __init__(self, brand, model, battery):
    super().__init__(brand, model)
    self.battery = battery

my_First_Electric_car = ElectricCar("Tesla","Model S","85KWH")
print(my_First_Electric_car.full_Name())
print(my_First_Electric_car.__brand)
print(my_First_Electric_car.get_brand())

# my_First_car = Car("TATA","Safari")  # This is instance 1
# print(my_First_car.brand)
# print(my_First_car.model)
# print(my_First_car.full_Name())

# my_second_car = Car("Toyota","Innova")  # This is instance 2
# print(my_second_car.brand)
# print(my_second_car.model)