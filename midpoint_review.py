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




# 4a.
# Hint: You can solve this problem without a forloop, but if you can figure it out using a for loop try to do it that way
# Write a program that asks the user to input how much money they have saved up. 
# Then ask the user to input a monthly growth rate (%) example: 5% would mean their savings would increase by 5% monthly. 
# Calculate how much the user would have at the end of each month for 12 months & print it all to the user

Money = input("How much money did you saved up: ")
Monthly_growth_rate = input("What is the monthtly growth rate(%): ")
mouth = 1

Monthly_growth_rate = int(Monthly_growth_rate)
Monthly_growth_rate = Monthly_growth_rate / 100
Money = int(Money)


while mouth <= 12:
    Money_after = Money + Money * Monthly_growth_rate
    print("In", mouth, "mouth, you have ", Money_after)

    mouth = mouth + 1
    Money = Money_after