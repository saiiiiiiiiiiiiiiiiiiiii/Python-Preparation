# Question on Conditionals
# Age Group Categorization
# Classify a person's age group : child(< 13), Teenager(13 - 19),Adult(20-59),Senior(+60)
# age = int(input("Enter you're age  "))
# if (age < 13):
#   print("Child")
# elif(age >= 13 and age <=19):
#   print("Teenager")
# elif(age >= 20 and age <=59):
#   print("Adult")
# elif(age >= 60):
#   print("Senior")


# age = int(input("Enter you're age   "))
# if age < 13:
#   print("Child")
# elif age <20:
#   print("Teenager")
# elif age <60:
#   print("Adult")
# else:
#   print("Senior")


# 2) Movie Ticiket Pricing 
# Movie Ticiket's are based on age : 12$ for adults(18 and over),8$ for children ,
# and Everyone get's Discount of 2 $ on Wednesday


# age = 26
# day = "Wednesday"
# price = 12 if age >= 18 else 8
# if day == "Wednesday":
#   price = price - 2
# print(price)





# 3)Grade Calculator
# Assign a Letter grade based on student's Score :A (90-100), B(80 - 89)
# C(70 - 79), D(60 - 69),F
# Score = int(input("Enter you're Marks:-   "))
# if Score >= 90:
#     grade = "A"
# elif Score >= 80:
#     grade = "B"
# elif Score >= 70:
#     grade = "C"
# elif Score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print("grade" , grade)


# 4)Fruit Ripeness Checker
# Determine if a fruit is ripe, overripe or unripe based on it's color 
# (eg Bananna : Green - Unripe, Yellow : Ripe , Brown - Overripe)

# fruit = "Bananna"
# color = "Green"

# if fruit == "Bananna":
#   if color == "Green":
#     print("unripe")
#   elif color == "Yellow":
#     print("Ripe")
#   elif color == "Brown":
#     print("Overripe")



# 5) Weather Activity Sugestion 
# Suggest an Activity based on the weather (eg, Sunny-Go for a walk ,Rainy -Read a book, Snowy - Build a Snowman)

# weather = "Rainy"
# if weather == "Sunny":
#   activity = "go for a walk"
# elif weather == "Rainy":
#   activity = "Read a Book"
# elif weather == "Snow":
#   activity = "Build a Snowman"

# print(activity)


#6) Transportation Mode Selection
# Choose a mode of Transport Based on the distance (eg.<3km: Walk)(3 - 15 km : Bike)(>15 km : car)

# distance = 2
# if distance < 3:
#   print("Walk")
# elif distance <= 15:
#   print("Bike")
# elif distance > 15:
#   print("Car")


# 7) Coffee Customization
# Customize an Coffee Order: "Small" "Medium" and "Large" with an Option for "Extra shot " of Espresso

# order_size = "Small"
# extra_shot = True
# if extra_shot:
#   coffee = order_size + "Coffee with an Extra Shot"
# else:
#   coffee = order_size + "Coffee"

# print(coffee)

# 8) password strength checker
# check if password is strong , medium or weak less than 6 means weak, 6 to 10 character's mean's medium , 
# more than 10 character's then strong 

# password = "Secure2p@ss"
# if len(password) < 6:
#   print("Weak")
# elif len(password)<= 10 :
#   print("medium")
# elif len(password) > 10:
#   print("Strong")


# 9)Leap year checker
# Determine if year is a leap year .(Leap year's are divisible by 4 , but no by 100 unless also divisible by 400)

# year = int(input("Enter a Year :-  "))
# if (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# elif (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


# 10) Pet food Recomandation
# Recommend a type of pet food based on the pet's specie's and age 
# e.g(Dog: < 2 yesr's - puppy food , Cat > 5 yesr's - Senior Cat food)

animal = input("what is you're pet:-  ")
age = int(input("what is your pet's age:-  "))
if  age <= 2:
  print("Puppy food")
elif age > 2:
  print("Senior Cat food")
