#homework
from turtle import *

length = int(input("what is the length of one side of your triangle? "))
        
def triangle(length):
    for counter in range(4):
        forward(length)
        left(120)

triangle(length)
