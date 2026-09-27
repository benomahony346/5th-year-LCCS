# 1. Fitness app
steps = 0
target = 10000

while steps < target:
    steps += 1000
    print("Steps:", steps)


# 2. Playlist
song = 1

while song <= 12:
    if song % 4 != 0:
        print("Now playing song", song)
    song += 1


# 3. Game
lives = 3
points = 0

while lives > 0:
    choice = input("Enter w to win or l to lose: ")

    if choice == "w":
        points += 10
    elif choice == "l":
        lives -= 1

print("Final score:", points)