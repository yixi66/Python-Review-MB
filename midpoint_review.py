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
# change type to calculation
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

mouth_list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
mouth = 0

# change type to calculation
Monthly_growth_rate = int(Monthly_growth_rate)
Monthly_growth_rate = Monthly_growth_rate / 100
Money = int(Money)


while mouth <= 12:
    for i in mouth_list:
        Money_after = Money + Money * Monthly_growth_rate
        print("In", i, "mouth, you have ", Money_after)

        mouth = mouth + 1
        Money = Money_after
    




# 4b.
# Now take the code you wrote for problem 4a and put it in a function called calc_investment(). It should take two parameters:
# the users savings and the growth rate. So it would look something like def calc_investment(savings, growth_rate):
# Once you have the function created call this function in your main with different savings and growth rate. 
# If you are unsure how to 'call' a function. All you have to do is type it out in your main.





# 5a. 
# create a list with 10 different employees salaries.
employees_salaries = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500]
# 5b. 
# print out the last item in your list
print (employees_salaries[-1])
# 5c. 
# print out indexes 2 through 8(make sure you include 8)
print (employees_salaries[1:9])
# 5d. 
# print out the entire list but skip every other value 
print(employees_salaries[0:11:2])
# 5e.
# print out the entire list in reverse order
print(employees_salaries[10:0:-1])
# 5f.
# add a new salary to the list
employees_salaries.append(6000)
print(employees_salaries)
# 5g. 
# create another list that stores every other salary from the original list: 
employees_salaries_2 = [1000, 2000, 3000, 4000, 5000]
# 5h. 
# remove an specific item from a list. 
employees_salaries.remove(2000)
print(employees_salaries)
# 5i.
# remove the last item in the list
employees_salaries.pop()
print(employees_salaries)




# 6a. 
# create another list filled with names corresponding to the salaries list you created in problem 5a.
# 5a list
employees_salaries = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500]
employees_names = ["Aaila", "Bobbe", "Carle", "Dennie", "Eita", "Faira", "Giorgia", "Hoby", "Ialen","Jenee"]
# 6b. 
# print out the length of your names list and your salary list. Make sure they're the same length
print(len(employees_salaries))
print(len(employees_names))
# 6c.
# using a for loop print out every name in your list
for n in employees_names:
    print (n)
## 6d. 
# using a for loop greet every person from your names list: 
for n in employees_names:
    print("Hi!",n)




# 7a. 
# create a list of bonuses$$
bonuses = [100, 200, 250, 500]
# 7b.
# import random 
# using the random library give random bonuses to the salaries list you created in problem 5. 
# You will need to loop through every single salary and add a random bonus to the original salary
import random
for i in employees_salaries:
    i = random.choice(bonuses) + i
    print(i)



# 8a.
# create a dictionary called employee_info and given it the initial value of {"your name": <your desired salary>}
employee_info = {"cathy":9000}
# 8b. 
# add 5 more employees to your dictionary with their own salaries
employee_info2 = {"Aaila":1000, "Bobbe":1500, "Carle":2000, "Dennie":2500, "Eita":3000}
employee_info.update(employee_info2)
# 8c. 
# print out every key in the dictionary
print(employee_info.keys())