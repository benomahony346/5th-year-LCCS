def median_odd(lst):
    middle = len(lst) // 2
    return lst[middle]


list1 = [2, 4, 7, 8, 10, 12]

print("Median of odd list:", median_odd(list1))

def median_even(lst):
    middle = len(lst) // 2
    return (lst[middle - 1] + lst[middle]) // 2


list2 = [2, 4, 7, 8, 10, 12, 14, 16]

print("Median of even list:", median_even(list2))