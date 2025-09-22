from turtle import *

## Task 1: Look at the following code and decide which picture it will generate.
# Then download it from the shared drive, then save and run it, to check.
speed(100)
def demo():
  pencolor("red")
  for counter in range (20):
    forward (150)
    right(100)

demo()

def dem():
  pencolor("blue")
  for counter in range (20):
    forward (150)
    right(100)

dem()
clear()
def deo():
  pencolor("orange")
  for counter in range (200):
    forward (150)
    right(95)

deo()

def emo():
  pencolor("red")
  for counter in range (20):
    forward (150)
    right(100)

emo()
clear()
#3.	The following code will draw a petal of a
#flower. Use the code in a for loop to make a
#flower as shown on the right.

def petal():
    circle(50,120)
    left(60)
    circle(50,120)

petal()
clear()

def flower():
    for counter in range (20):
        petal()

flower()
clear()
#1.	Modify your square function so that you can input the length of the sides and draw squares of different sizes
length = int(input("what is the length of one side of your square? "))
import turtle
        
def square(length):
    for counter in range(4):
        turtle.forward(length)
        turtle.left(90)

square(length)
turtle.done()
