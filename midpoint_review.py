# 1.
# Create Input Variables for your first name, last name and age.
# Then print out your full name and age within a sentence

first_name = input("What is your first name: ")
Last_name = input("What is your last name: ")
age = input("Enter your age: ")

print("My name is " ,first_name + Last_name, ", I am " ,age ," years old")




# 2. 
# create 3 different variables with any whole number assined as the value and convert them into a string using the str() constructor.
# once you convert them print out the variables. Example: convert 3 to '3'
# if you use print(type(<var_name>)) this will print out the type of variable for example x = 3 would print 'int' and x = '3' would print 'str'

number=[4, 25, 68]
# int
print(number)
# str
print(str(number))




# 3.
# Write a program that asks the user for the current temperature (F) and then use their Input calculate temperature in (C). 
# Here is the formula to conver F to C => C = (Fahrenheit - 32) * 5.0/9.0
# Once you calculate Celcius print out the conversion to the user

temperature_F = input("What is the current Fahrenheit？")
# change type to int
temperature_F = int(temperature_F)
temperature_C = (temperature_F - 32)* 5.0/9.0
print(str(temperature_C))