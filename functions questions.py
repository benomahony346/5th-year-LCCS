# Q1: Addition and Subtraction

def calculation(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)

calculation(20, 10)


# Q2: Print Name and Age

def demo(name, age):
    print("Name:", name)
    print("Age:", age)

demo("John", 25)


# Q3: Check Employee Salary

def show_employee(name, salary):
    if salary > 40000:
        print(name + ", you are well paid")
    else:
        print(name + ", you are not well paid")

show_employee("John", 45000)


# Q4: Find Maximum of Three Numbers

def findMax(a, b, c):
    if a >= b and a >= c:
        print("Maximum number is:", a)
    elif b >= a and b >= c:
        print("Maximum number is:", b)
    else:
        print("Maximum number is:", c)

findMax(10, 25, 15)


# Q5: Reverse a String

def reverseString(string):
    print("Reversed string:", string[::-1])

reverseString("Python")