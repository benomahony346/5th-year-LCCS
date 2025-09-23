# 23rd september
from turtle import *


        
def triangle(length):
    for counter in range(3):
        forward(length)
        left(120)

       
def square(length):
    for counter in range(4):
        forward(length)
        right(90)

      
length = int(input("what is the length of one side of your triangle? "))
triangle(length)

length = int(input("what is the length of one side of your square? "))

square(length)

right(90)
forward(200)
left(90)
forward(75)
    
length2 = int(input("what is the length of one side of your square? "))
square(length2)