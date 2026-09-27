import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print(dice1)
print(dice2)

if dice1 != dice2:
    score = dice1 + dice2
    print(score)
else:
    score = (dice1 + dice2) * 2
    print("You threw a double")
    print(score)
