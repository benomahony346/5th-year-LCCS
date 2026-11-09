def calculate_area(radius):
    area = 3.14 * radius * radius
    return area

print(calculate_area(5))
print(calculate_area(10))
print(calculate_area(7))

#4
def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

print(calculate_rectangle_properties(5, 3))
print(calculate_rectangle_properties(10, 4))
print(calculate_rectangle_properties(7, 2))

#5
def is_valid_temperature(temperature):
    if -50 <= temperature <= 50:
        return True
    else:
        return False

print(is_valid_temperature(25))
print(is_valid_temperature(60))
print(is_valid_temperature(-30))