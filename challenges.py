# Challenge 045

total = 0

while total < 50:
    number = int(input("Enter a number: "))
    total = total + number
    print("The total is", total)
# Challenge 046

number = int(input("Enter a number: "))

while number <= 5:
    number = int(input("Enter a number: "))

print("The last number you entered was", number)
# Challenge 047

total = 0

number = int(input("Enter a number: "))
total = total + number

answer = input("Do you want to enter another number? (y/n): ")

while answer == "y":
    number = int(input("Enter another number: "))
    total = total + number
    answer = input("Do you want to enter another number? (y/n): ")

print("The total is", total)
# Challenge 048

name = input("Enter the name of somebody you want to invite: ")

while name != "":
    print(name, "has now been invited")
    name = input("Enter another name: ")

print("The party invitation list is complete.")
# Challenge 049

compound = 50
attempts = 0

number = int(input("Enter a number: "))
attempts = attempts + 1

while number != compound:
    if number < compound:
        print("Too low")
    else:
        print("Too high")

    number = int(input("Enter another number: "))
    attempts = attempts + 1

print("Well done, you took", attempts, "attempts")
# Challenge 050

number = int(input("Enter a number between 10 and 20: "))

while number < 10 or number > 20:
    if number < 10:
        print("Too low")
    else:
        print("Too high")

    number = int(input("Try again: "))

print("Thank you")
# Challenge 051

bottles = 10

while bottles > 0:
    print("There are", bottles, "green bottles hanging on the wall.")
    print("There are", bottles, "green bottles hanging on the wall.")
    print("And if one green bottle should accidentally fall...")

    answer = int(input("How many green bottles will be hanging on the wall? "))

    while answer != bottles - 1:
        print("No, try again")
        answer = int(input("How many green bottles will be hanging on the wall? "))

    bottles = bottles - 1

print("There are no more green bottles hanging on the wall.")