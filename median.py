list = [2, 4, 6, 8, 10]
find = 4 

    # Find median of the list
if len(list) % 2 == 0:
    print(len(list), "This has an even number of entries")
    median = (len(list) // 2) - 1
else:
    print(len(list), "This has an odd number of entries")
    median = len(list)// 2
    
print("The index of the median is", median)

print("Value at median location is", list[median])

while find != list[median]:
    if find == list[median]:
        print("value found")
        
    elif find < list[median]:
        list = list[(median+1):]
        print(list)
        
    elif find > list[median]:
        list = list[:median]
        print(list)
        
        
    else:
        print("value isnt in list")
        break
