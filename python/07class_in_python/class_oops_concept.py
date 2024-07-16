# 1) Basic class and object 
# create a car class with attributes like brand and model Then create an instance of the class 
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

# my_first_car = Car("Tata","safari")  # This is an instance mean's Object which created by the class name Car
# print(my_first_car.brand)
# print(my_first_car.model)


# 2) Class Method and Self
# Add a Method to the Car Class That displays the full name of the car
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def Full_name(self):    # This is what we add a Method (a Function) That display's a Full name of the car
#     return f"{self.brand} {self.model}"

# my_first_car = Car("Tata", "Safari")
# print(my_first_car.brand)
# print(my_first_car.model)
# print(my_first_car.Full_name())

# 3) Inheritence
# Create an Electric Class that inherits from the Car Class and has an additional attribute 
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def Full_name(self):
#     return F"{self.brand} {self.model}"

# class Electriccar(Car):
#   def __init__(self, brand, model, battery):  # First We have to initalize the attribute's in the inherit (inheritence) class and then we have to check that which attributes we have to take from the parent class by using super() Keyword
#     self.battery = battery
#     super().__init__(brand , model)

# my_first_electric_car = Electriccar("Tata Motors", "Altroz hatchback", "Altroz's lithium-ion battery pack ")
# print(my_first_electric_car.brand)
# print(my_first_electric_car.model)
# print(my_first_electric_car.battery)


# class Car:
#   def __init__(self, brand ,model):
#     self.brand = brand
#     self.model = model

#   def Full_name(self):
#     return f"{self.brand} {self.model}"

# class Electriccar(Car):
#   def __init__(self, brand, model, battery):
#     self.battery = battery
#     super().__init__(brand , model)

# my_First_Electric_car = Electriccar("Mahindra", "XUV300", "Lithium-ion batteries")
# print(my_First_Electric_car.brand)
# print(my_First_Electric_car.model)
# print(my_First_Electric_car.battery)



# Encapsulation
# Modify The Car class to encapsulate the brand attribute making it private and provide a getter method for it

# class Car:
#   def __init__(self, brand, model):
#     self.__brand = brand
#     self.model = model

#   def Full_name(self):
#     return f"{self.__brand} {self.model}"
  
#   def get__brand(self):
#     return self.__brand + " !"
  
  
  
# class ElectricCar(Car):
#   def __init__(self, brand, model, battery):
#     self.battery = battery
#     super().__init__(brand, model)


# my_first_electric_car = ElectricCar("Tata Motors", "Altroz hatchback", "lithium-ion battery pack")
# print(my_first_electric_car.get__brand())
# # print(my_first_electric_car.__brand)
# # print(my_first_electric_car.model)
# # print(my_first_electric_car.battery)

# class Car:
#   def __init__(self, brand, model):
#     self.__brand = brand
#     self.model = model

#   def Full_name(self):
#     return f"{self.__brand} {self.model}"
  
#   def get_brand(self):
#     return self.__brand + " !"

# class Electriccar(Car):
#   def __init__(self, brand, model,battery):
#     self.battery = battery
#     super().__init__(brand, model)

# my_first_EV_Car = Electriccar("Tata Motors", "new Altroz hatchback.", "Altroz's lithium-ion battery pack ")
# print(my_first_EV_Car.model)
# print(my_first_EV_Car.battery)
# print(my_first_EV_Car.get_brand())
# print(my_first_EV_Car.get_brand())


# Polymorphism
# Demonstrate polymorphism by defining a method fuel_type in both Car and Electric_Car classes , but with different behaviour's
# class Car:

#   def __init__(self, brand, model):
#     self.__brand = brand
#     self.model = model


#   def Full_name(self):
#     return f"{self.__brand} {self.model}" 
  
#   def get_brand(self):
#     return self.__brand + " !"
  
#   def Fuel_type(self):
#     return "Petrol or Diesel"
  
# class Electriccar(Car):
#   def __init__(self, brand, model , battery):
#     self.battery = battery
#     super().__init__(brand, model)

#   def Fuel_type(self):
#     return "Electric Battery "

# Ev_car = Electriccar("Tata Motors", "Altroz hatchback", "Altroz's lithium-ion battery pack")
# # print(Ev_car.brand) 
# # print(Ev_car.get_brand())
# # print(Ev_car.model)
# # print(Ev_car.battery)
# # print(Ev_car.Fuel_type())

# car = Car("Tata Motors", "Safari")
# print(car.Fuel_type())
# print(car.get_brand())
# print(car.model)




# 6) Class Variable
# Add a class variable to Car that  keeps track of the number of the cars created .

# class Car:
#   total_car = 0
#   def __init__(self, brand, model):
#     self.__brand = brand
#     self.model = model
#     Car.total_car += 1

#   def Full_name(self):
#     return f"{self.__brand} {self.model}" 
  
#   def get_brand(self):
#     return self.__brand + " !"
  
#   def Fuel_type(self):
#     return "Petrol or Diesel"
  
# class Electriccar(Car):
#   def __init__(self, brand, model , battery):
#     self.battery = battery
#     super().__init__(brand, model)

#   def Fuel_type(self):
#     return "Electric Battery "

# Ev_car = Electriccar("Tata Motors", "Altroz hatchback", "Altroz's lithium-ion battery pack")
# # print(Ev_car.brand) 
# # print(Ev_car.get_brand())
# # print(Ev_car.model)
# # print(Ev_car.battery)
# # print(Ev_car.Fuel_type())

# car = Car("Tata Motors", "Safari")
# print(car.Fuel_type())
# print(car.get_brand())
# print(car.model)
# print(Car.total_car)


# 7) Static Method
# Add a static Method to the car Class that return's a general desciription of car 
# class Car:
#   total_car = 0
#   def __init__(self, brand, model):
#     self.__brand = brand
#     self.model = model
#     Car.total_car += 1

#   def Full_name(self):
#     return f"{self.__brand} {self.model}" 
  
#   def get_brand(self):
#     return self.__brand + " !"
  
#   def Fuel_type(self):
#     return "Petrol or Diesel"
  
#   @staticmethod   # This is Decorator's in python @ when we use a keyword "@staticMethod" then we don't need to use the self keyword in the placeholder
#   def general_descripition():
#     return "This is a general description of car That Car is a mean's of Transport"
  
# class Electriccar(Car):
#   def __init__(self, brand, model , battery):
#     self.battery = battery
#     super().__init__(brand, model)

#   def Fuel_type(self):
#     return "Electric Battery "

# Ev_car = Electriccar("Tata Motors", "Altroz hatchback", "Altroz's lithium-ion battery pack")
# # print(Ev_car.brand) 
# # print(Ev_car.get_brand())
# # print(Ev_car.model)
# # print(Ev_car.battery)
# # print(Ev_car.Fuel_type())

# car = Car("Tata Motors", "Safari")
# print(car.Fuel_type())
# print(car.get_brand())
# print(car.model)
# print(Car.total_car)
# print(car.general_descripition())

# 8) Property Decorator's 
# Use a property decorator in the Car class to make the model attribute read_only 

# class Car:
#   total_car = 0
#   def __init__(self, brand, model):
#     self.__brand = brand
#     self.__model = model
#     Car.total_car += 1

#   def Full_name(self):
#     return f"{self.__brand} {self.__model}" 
  
#   def get_brand(self):
#     return self.__brand + " !"
  
#   def Fuel_type(self):
#     return "Petrol or Diesel"
  
#   @staticmethod   # This is Decorator's in python @ when we use a keyword "@staticMethod" then we don't need to use the self keyword in the placeholder
#   def general_descripition():
#     return "This is a general description of car That Car is a mean's of Transport"
  
#   @property
#   def model(self):
#       return self.__model
  
# class Electriccar(Car):
#   def __init__(self, brand, model , battery):
#     self.battery = battery
#     super().__init__(brand, model)

#   def Fuel_type(self):
#     return "Electric Battery "

# Ev_car = Electriccar("Tata Motors", "Altroz hatchback", "Altroz's lithium-ion battery pack")
# # print(Ev_car.brand) 
# # print(Ev_car.get_brand())
# # print(Ev_car.model)
# # print(Ev_car.battery)
# # print(Ev_car.Fuel_type())

# car = Car("Tata Motors", "Safari")
# # car.model = "nano"
# # print(car.Fuel_type())
# # print(car.get_brand())
# print(car.model)
# # print(Car.total_car)
# # print(car.general_descripition())


# 9) Class inheritence and isinstacnce () Function
# Problem Demonstrate the use of instance() to check if my_tesla is an instacnce of Car and Electric Car

# class Car:
#   total_car = 0
#   def __init__(self, brand, model):
#     self.__brand = brand
#     self.__model = model
#     Car.total_car += 1

#   def Full_name(self):
#     return f"{self.__brand} {self.__model}" 
  
#   def get_brand(self):
#     return self.__brand + " !"
  
#   def Fuel_type(self):
#     return "Petrol or Diesel"
  
#   @staticmethod   # This is Decorator's in python @ when we use a keyword "@staticMethod" then we don't need to use the self keyword in the placeholder
#   def general_descripition():
#     return "This is a general description of car That Car is a mean's of Transport"
  
#   @property
#   def model(self):
#       return self.__model
  
# class Electriccar(Car):
#   def __init__(self, brand, model , battery):
#     self.battery = battery
#     super().__init__(brand, model)

#   def Fuel_type(self):
#     return "Electric Battery "
  


# Ev_car = Electriccar("Tata Motors", "Altroz hatchback", "Altroz's lithium-ion battery pack")
# # print(Ev_car.brand) 
# # print(Ev_car.get_brand())
# # print(Ev_car.model)
# # print(Ev_car.battery)
# # print(Ev_car.Fuel_type())

# car = Car("Tata Motors", "Safari")
# print(isinstance(Ev_car, Car))
# print(isinstance(car, Car))
# # car.model = "nano"
# # print(car.Fuel_type())
# # print(car.get_brand())
# print(car.model)
# # print(Car.total_car)
# # print(car.general_descripition())


# 10) Multiple inheritence
# Create Two Classses Battrey and engine and let the electric car class inherit from the both ,demonstrationg multipple inheritance



# class Car:
#   total_car = 0
#   def __init__(self, brand, model):
#     self.__brand = brand
#     self.__model = model
#     Car.total_car += 1

#   def Full_name(self):
#     return f"{self.__brand} {self.__model}" 
  
#   def get_brand(self):
#     return self.__brand + " !"
  
#   def Fuel_type(self):
#     return "Petrol or Diesel"
  
#   @staticmethod   # This is Decorator's in python @ when we use a keyword "@staticMethod" then we don't need to use the self keyword in the placeholder
#   def general_descripition():
#     return "This is a general description of car That Car is a mean's of Transport"
  
#   @property
#   def model(self):
#       return self.__model
  
# class Electriccar(Car):
#   def __init__(self, brand, model , battery):
#     self.battery = battery
#     super().__init__(brand, model)

#   def Fuel_type(self):
#     return "Electric Battery "
  


# class Battery:
#   def __init__(self, battery_type, battery_size):
#     self.battery_type = battery_type
#     self.battery_size = battery_size


# class Engine:
#   def __init__(self, engine_type, engine_size):
#     self.engine_type = engine_type
#     self.engine_size = engine_size

#   def engine(self):
#     return "I Am the Description of Engine Class"



# class Electric_Car_two(Battery,Engine,Car):
#   # def __init__(self, engine_type, engine_size, battery_type, battery_size, brand):
#   #   self.brand = brand
#   #   super().__init__(engine_size, engine_type, battery_type,battery_size)
#   pass

# Ev_car = Electric_Car_two("Tast", "ujsadcvv")
# # print(Ev_car.Fuel_type())
# print(Ev_car.battery_size)
# print(Ev_car.battery_type)
# print(Ev_car.engine())

# Ev_car = Electriccar("Tata Motors", "Altroz hatchback", "Altroz's lithium-ion battery pack")
# # print(Ev_car.brand) 
# # print(Ev_car.get_brand())
# # print(Ev_car.model)
# # print(Ev_car.battery)
# # print(Ev_car.Fuel_type())

# car = Car("Tata Motors", "Safari")
# # print(isinstance(Ev_car, Car))
# # print(isinstance(car, Car))
# # car.model = "nano"
# # print(car.Fuel_type())
# # print(car.get_brand())
# # print(car.model)
# # print(Car.total_car)
# # print(car.general_descripition())




class First_Class:
  def Method_First(self):
    return "I am the first Method from first class"

class Second_Class:
  def Method_Second(self):
    return "I am the Second Method from Second class"
  

class Third_Class(First_Class, Second_Class):
    def Method_Third(self):
      return "I am the Second Method from Second class"


# obj = Third_Class()

# print(obj.Method_First())
# print(obj.Method_Third())

