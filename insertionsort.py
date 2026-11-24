numbers = [12, 34, 5, 8, 16]

print("Starting list:", numbers)

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1

    print("\nInserting:", key)

    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        print("Moving", numbers[j], numbers)
        j -= 1

    numbers[j + 1] = key

    print( key, numbers)

print("\nFinal sorted list:", numbers)
