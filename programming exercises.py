#25 sep 25
# ben holland

#question1
# this program calculates the given values to a total 
costOfCoke = 4 * 1.5
qtyCrisps = 3
costOfBread = 3.50
qtyMars = 5
costOfTea = 2 * 2
unitCostOfCrisps = 0.8
costOfMars = qtyMars * 1
costOfCrisps = qtyCrisps * unitCostOfCrisps
total = costOfMars+costOfCoke+costOfCrisps+costOfTea+costOfBread
print("the total cost is", total)

#question 2
number1 = int(input("enter the first number: "))
number2 = int(input("enter the secound number: "))
sum = number1 + number2
print("the answer is", sum)


dd = int(input("day: "))
mm = int(input("month: "))
y = int(input("year: "))
c = 
w = (dd + (13*(mm + 1)/5) + y + (y/4) + (c/4) - 2*c)%7