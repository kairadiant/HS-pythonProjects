from turtle import *
#to move
def movefd(x):
   pu()
   fd(x)
   pd()
#to keep track of the heading
def go(p):
   pu()
   goto(p)
   pd()
   setheading(0)
#for the spaces between the numbers
def space(x):
   movefd(1.5*x)
# Functions for the numbers
def zero(x):
   for i in range(2):
       fd(x)
       rt(90)
       fd(2*x)
       rt(90)

def one(x):
   start = pos()
   movefd(x)
   rt(90)
   fd(2*x)
   go(start)

def two(x):
   start = pos()
   fd(x)
   rt(90)
   fd(x)
   rt(90)
   fd(x)
   lt(90)
   fd(x)
   lt(90)
   fd(x)
   go(start)

def three(x):
   start = pos()
   fd(x)
   rt(90)
   fd(x)
   rt(90)
   fd(x)
   bk(x)
   lt(90)
   fd(x)
   rt(90)
   fd(x)
   go(start)

def four(x):
   home = pos()
   movefd(x)
   rt(90)
   fd(2*x)
   go(home)
   rt(90)
   fd(x)
   lt(90)
   fd(x)
   go(home)

def five(x):
   home = pos()
   fd(x)
   bk(x)
   rt(90)
   fd(x)
   lt(90)
   fd(x)
   rt(90)
   fd(x)
   rt(90)
   fd(x)
   go(home)

def six(x):
   home = pos()
   rt(90)
   fd(2*x)
   lt(90)
   fd(x)
   lt(90)
   fd(x)
   lt(90)
   fd(x)
   go(home)
   fd(x)
   go(home)

def seven(x):
   home = pos()
   fd(x)
   rt(90)
   fd(2*x)
   go(home)

def eight(x):
   home = pos()
   for i in range(4):
       fd(x)
       rt(90)
   for i in range(2):
       fd(x)
       rt(90)
       fd(2*x)
       rt(90)
   go(home)

def nine(x):
   home = pos()
   fd(x)
   rt(90)
   fd(2*x)
   rt(90)
   fd(x)
   go(home)
   for i in range(4):
       fd(x)
       rt(90)

#moves turtle so whole sentence fits
def moveto(x,y):
    pu()
    goto(x,y)
    pd()