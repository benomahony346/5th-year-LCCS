# Question 1

steps = 0

while steps < 10000:
    steps = steps + 1000
    print(steps)
# Question 2

for song in range(1, 13):
    if song % 4 == 0:
        continue
    print("Now playing song", song)