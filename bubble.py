def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            # Step 1: Compare two adjacent elements
            if arr[j] > arr[j + 1]:

                # Step 2: Swap if the first is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Step 5: Return the sorted array
    return arr


# Input array
numbers = [64, 34, 25, 12, 22, 11, 90]

# Sort the array
sorted_numbers = bubble_sort(numbers)

# Display the result
print("Sorted Array:", sorted_numbers)