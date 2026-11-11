list = [1, 2, 3, 4]

#find the median of the list

if len(list) % 2 == 0:
    print(len(list), "this has an even number of entries")
    median = len(list)//2 - 1
    print(median)
    
else:
    print(len(list), "this has an odd number of entries")
    median = len(list)//2
    print(median)

print ("value at median location is ", list[median])