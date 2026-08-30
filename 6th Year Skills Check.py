# 6th Year Python Skills
# Name: Ben holland omahony 

# print("Welcome to the Python Skills Check!")
# 
# print("task 1 ")
# message = "python is fun!"
# print(message)
# print ("today is wednesday")
# 
# colour = input("please enter your favourite colour : ")
# movie = input("please enter your favourite movie : ")
# 
# print(" your favorite colour is", colour, "your favorite movie is", movie)
# 
# age = input ("what is your age :")
# year = input ("what year were you born : ")
# 
# print ("you are", age , "years old and were born in", year)
# 
# cost = float(input("how much does the item cost : "))
# ammount = float(input("how much of the item are you getting : "))
# total = float(cost * ammount)
# # print("your total is ",total)
# 
# num1 = 12
# num2 = 4
# 
# print("add=",num1+num2,)
# print("sub=",num1-num2,)
# print("multiply=",num1*num2,)
# print("division=",num1/num2,)


# Task 6 - If Statements

number = int(input("Please enter a number: "))

if number > 0:
    print(number, "is a positive number")
elif number < 0:
    print(number, "is a negative number")
else:
    print(number, "is equal to zero")


# Task 7 - Area of a Rectangle

length = float(input("Please enter the length: "))
width = float(input("Please enter the width: "))

area = length * width

print("The area is:", area)