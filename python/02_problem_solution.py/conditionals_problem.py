# question on conditional's
# 1) Age group categorization
# Classify a person's age group : Child(<13), Teeneager(13 - 19),Adult(20-59),(senior(60 +))
# age = int(input("Please Enter you're age  "))
# if age < 13:
#   print("You are a child")
# elif age >= 13 and age <= 19:
#   print("You are a teenager")
# elif age >= 20 and age <= 59:
#   print("You are an adult")
# elif age >= 60:
#   print("You are a senior")


# 2) Movie Ticiket Pricing 
# The Prices of Movie Ticikets Based on age : 12$ for adult's(18 and over) , 
# 8$ for Children . Everyone get's a 2$ discount on wednesday

# age = int(input("Enter You're age  "))
# Day = input("Enter Today's Day   ")
# if age >=18:
#     if Day == "Wednesday":
#         print("Today is Wednesday so Ticiket Fare will be 10 $")
#     else: 
#         print("Today Ticiket fare will be 12$")
        

# if age <=17:
#     if Day == "Wednesday":
#         print("Today is Wednesday so Ticiket Fare will be 6 $")
#     else:
#         print("Today Ticiket fare will be 8$")


# 3)Grade Calculator
# Assign a Letter grade based on student's Score :A (90-100), B(80 - 89)
# C(70 - 79), D(60 - 69),F

# marks = int(input("Enter your marks  ")) 
# if marks >= 90 and marks < 100:
#   print("A Grade")
# elif marks >= 80 and marks <= 89:
#   print("B Grade")
# elif marks >= 70 and marks <= 79:
#   print("C Grade")
# else:
#   print("F Grade")

# 4)Fruit Ripeness Checker
# Determine if a fruit is ripe, overripe or unripe based on it's color 
# (eg Bananna : Green - Unripe, Yellow : Ripe , Brown - Overripe)

# fruit = input("What is the name of the fruit :-  ")
# condition_by_color = input("What is the color condiiton of the fruit:-  ")
# if condition_by_color == "Green" or condition_by_color ==  "Greenish" or condition_by_color == "green" or condition_by_color == "greenish":
#        print(f"The {fruit} is unripe")
# elif condition_by_color == "Yellow" or condition_by_color == "Yellowish" or condition_by_color == "yellow" or condition_by_color == "yellowish": 
#     print(f"The {fruit} is ripe")
# elif condition_by_color == "Brown" or condition_by_color == "Brownish" or condition_by_color == "brown" or condition_by_color == "brownish" :
#     print(f"The {fruit} is Overripe")


# Weather Activity Sugestion 
# Suggest an Activity based on the weather (eg, Sunny-Go for a walk ,Rainy -Read a book, Snowy - Build a Snowman)

# weather_condition = input("How's Weather:-  ")
# if weather_condition == "Sunny" or weather_condition == "sunny":
#   print(" Okay then if it's sunny then Go for a walk")
# elif weather_condition == "Rainy" or weather_condition == "rainy":
#   print(" Okay then if it's Rainy then  Read a book")
# elif weather_condition == "Snowy" or weather_condition == "snowy" or weather_condition == "Snowish"  or weather_condition == "snowish" or weather_condition == "Snow" or weather_condition == "snow":
#   print(" Okay then if it's Snow then Enjoy Build a Snowman")


# 6) Transportation Mode Selection
# Choose a mode of Transport Based on the distance (eg.<3km: Walk)(3 - 15 km : Bike)(>15 km : car)
# Distance = int(input("Enter How many km of distances you want to travel:-    "))
# if Distance <= 3:
#   print("Okay then you can walk")
# elif Distance > 3 and Distance <= 15:
#   print("Okay then you can use Bike")
# elif Distance > 15 :
#   print("Okay then you can use Car")


# 7) Coffee Customization
# Customize an Coffee Order: "Small" "Medium" and "Large" with an Option for "Extra shot " of Espresso
# Size = input("What size of coffee you want:-  ")
# Enquiry_for_Espresso = input("Do you Want an Extra Shot of Espresso : -")
# if Size == "Small" or Size == "small":
#     if Enquiry_for_Espresso == "Yes" or Enquiry_for_Espresso == "yes":
#         print("Okay then you can have a Small Coffee with an Extra Shot of Espresso")
#     else:
#         print("Okay then you can have a Small Coffee")

# if Size == "Medium" or Size == "medium":
#     if Enquiry_for_Espresso == "Yes" or Enquiry_for_Espresso == "yes":
#         print("Okay then you can have a Medium Coffee with an Extra Shot of Espresso")
#     else:
#         print("Okay then you can have a Medium Coffee")

# if Size == "Large" or Size == "large":
#     if Enquiry_for_Espresso == "Yes" or Enquiry_for_Espresso == "yes":
#         print("Okay then you can have a Large Coffee with an Extra Shot of Espresso")
#     else:
#         print("Okay then you can have a Large Coffee")





# 8) password strength checker
# check if password is strong , medium or weak less than 6 means weak, 6 to 10 character's mean's medium , 
# more than 10 character's then strong 
# password = input("Enter your password:- ")
# if password.__len__ ()< 6:
#   print("Your password is weak")
# elif password.__len__() <= 10:
#   print("Your password is medium")
# elif password.__len__() > 10 :
#   print("Your password is strong")


# 9)Leap year checker
# Determine if year is a leap year .(Leap year's are divisible by 4 , but no by 100 unless also divisible by 400)


# year = int(input("Enter the year:- "))

# if year % 4 == 0 and year % 100 != 0:
#     print("The year is a leap year")
# elif year % 400 == 0:
#     print("The year is a leap year")
# else:
#     print("The year is not a leap year")

# 10) Pet food Recomandation
# Recommend a type of pet food based on the pet's specie's and age 
# e.g(Dog: < 2 yesr's - puppy food , Cat > 5 yesr's - Senior Cat food)

pet_species = input("What is the species of animal:-    ")
old = int(input("How many year's old is the pet :-   "))
if (old <= 2):
  print(f"The {pet_species} is a puppy giv them a puppy food")
elif (old > 3):
  print(f"The {pet_species} is a senior giv them a senior food")















#This is also one of the approach to solve the problem 
# age = int(input("Enter You're age  "))
# Day = input("What is Today's Day  ")
# price = 12 if age >= 18 else 8
# if Day == "Wednesday":
#   price = price - 2
# print("You're Ticiket price will be", price)

