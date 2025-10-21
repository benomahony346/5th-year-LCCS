#exercise 1.1
student_name = input("what is your name: ")# asks your nme 
student_age = int(input("what is your age: "))# asks your age 
student_height = float(input("waht is your height: "))# asks your height 

print(" your name is", student_name, "=", type(student_name))# prints student name and what it is  
print(" your age is", student_age, "=", type(student_age))# prints student age and what it is
print(" your height is", student_height, "=", type(student_height))#prints student height and what it is

#1.2
current_year = 2025# current year 
your_year = int(input("what year were you born: ")) # asks you the year you were born 
there_age = print(" your age is ", current_year - your_year)# takes away both varibles and prints your age 

#1.3
n1 = int(input("Enter first number: "))
n2 = int(input("Enter secound number: "))
sum = n1 + n2
diffrence = n1-n2
product = n1*n2
division = n1/n2 
floor_division = n1//n2
remainder = n1%n2 