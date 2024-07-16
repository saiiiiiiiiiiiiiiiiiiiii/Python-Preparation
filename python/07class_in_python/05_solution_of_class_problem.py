# Polymorphism
# Demonstrate polymorphism by defining a method fuel_type in both Car and Electric_Car classes , but with different behaviour's

class Car:
  def __init__(self, brand,model):
    self.brand = brand  # This is attribute 
    self.model = model  # This is attribute

  def full_Name(self):
    return f"{self.brand} {self.model}"
  
  def fuel_type(self):
    return "Petrol or Diesel"
  
class ElectricCar(Car):
  def __init__(self, brand, model, battery):
    super().__init__(brand, model)
    self.battery = battery

  def fuel_type(self):
    return "Electric charge"
  


# my_First_car = Car("Tata","Safari")
# print(my_First_car.fuel_type())
my_first_Electric_car = ElectricCar("Tesla","Model s","90KWH")
print(my_first_Electric_car.fuel_type())


# my_First_Electric_car = ElectricCar("Tesla","Model S","85KWH")
# print(my_First_Electric_car.full_Name())
# print(my_First_Electric_car.brand)
# print(my_First_Electric_car.model)
# print(my_First_Electric_car.battery)

# my_First_car = Car("TATA","Safari")  # This is instance 1
# print(my_First_car.brand)
# print(my_First_car.model)
# print(my_First_car.full_Name())

# my_second_car = Car("Toyota","Innova")  # This is instance 2
# print(my_second_car.brand)
# print(my_second_car.model)