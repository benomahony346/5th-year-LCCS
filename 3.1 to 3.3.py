#question 1
score = float(input(" enter your score: "))
if score < 0 or score > 100:
    print("invalid score")
else:
    if score >= 90:
        grade = "a"
    elif score >= 80:
        grade = "b"
    elif score >= 70:
        grade = "c"
    elif score >= 60:
        grade = "d"
    else:
        grade = "f"
# question 2     
    print("your grade is: ",(grade))
    
year = int(input("enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 ):
    print((year), "is a leap year")
else:
    print((year), " is not a leap year")
    


# question 3
age = int(input("enter your age: "))
premium =input(" is this a premium showing yes or no: ").lower()

if age < 12:
    price = 6.50
elif age <= 17:
    price = 8.00
elif age <= 64:
    price = 12.00
else:
    price = 7.50
    
if premium == "yes":
    price += 3.00
    
print(" the total ticket price is:: ", (price))