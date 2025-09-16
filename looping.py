#16/9/25
#author ben holland
# looping 

# program written for Session 4

# Anything written after # is ignored by the computer
# We can use it to annotate programs to make them more readable

from turtle import *

# this line says we are using the "turtle" library of functions
# remember to use this for turtle graphics in Python
# program written for Session 4
# Anything written after # is ignored by the computer
# We can use it to annotate programs to make them more readable

from turtle import *

# this line says we are using the "turtle" library of functions
# dont remember to use this for turtle graphics in Python

def square ():
    #fillcolor("Green")
    begin_fill()
    pencolor("Red")
    forward (100) 
    right (90)
    end_fill()
    forward (100) 
    right (90) 
    forward (100) 
    right (90) 
    forward (100) 

square()


def mystery():
    #fillcolor("Green")
    begin_fill()
    pencolor("Red")
    forward (100) 
    right (45)
    end_fill()
    forward (100) 
    right (45) 
    forward (100) 
    right (45) 
    forward (100) 
    right (45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    
mystery()

#1 turn 90 degrees right 
#2 it goes forward 100 spaces 
#3 it dosent work 
#4 it makes it turn 45 degrees insted of 90
#5 say backwards and left 
#6 def defines the function 
#7 it dosent work
def triangle():
    pencolor("blue")
    forward(100)
    right(60)
    forward(100)
    right(60)
    forward(100)
    right(60)
    
triangle()