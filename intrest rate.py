#date 4th sep 25
# author ben holland
# ask the user for the princple
principal = input ("enter principal: ")
principal = float (principal)

#ask the user for the intrest rate
rate = input ("enter rate: ")
rate = float (rate)

#ask the user for the lenght of time
time = input ("enter time in years: ")
time = float(time)

#simple intrest calculation
amount = time * rate * principal

# display the answer
print(" the intrest amount is", amount)