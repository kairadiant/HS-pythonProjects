from turtle import *
from math import *
def movefd(x): #function to move
    pu()
    fd(x)
    pd()

def go(p): #function to return back to original position
    pu()
    goto(p)
    pd()
    setheading(0)

def space(x): # for spacing in between the letters
   movefd(1.5*x)

 #These are the functions for the different letters
def B(x):
    home = pos()
    fd(x/5)
    circle(-x/2,180)
    fd(x/5)
    rt(90)
    fd(x)
    bk(x)
    rt(90)
    fd(x/5)
    circle(-x/2,180)
    fd(x/5)
    rt(90)
    fd(2*x)
    go(home)

def D(x):
    home = pos()
    rt(90)
    fd(2*x)
    lt(90)
    fd(x/5)
    circle(x,180)
    fd(x/5)
    go(home)

def F(x):
    home = pos()
    fd(x)
    bk(x)
    rt(90)
    fd(x/2)
    lt(90)
    fd(x/2)
    bk(x/2)
    rt(90)
    fd(3*x/2)
    go(home)

def H(x):
    home = pos()
    rt(90)
    fd(2*x)
    bk(x)
    lt(90)
    fd(x)
    lt(90)
    fd(x)
    bk(x*2)
    go(home)

def J(x):
    home = pos()
    rt(90)
    fd(2*x)
    circle(-x/2,180)
    go(home)

def L(x):
    home = pos()
    rt(90)
    fd(2*x)
    lt(90)
    fd(x)
    go(home)

def N(x):
    home = pos()
    rt(90)
    fd(2*x)
    bk(2*x)
    lt(90)
    pu()
    fd(x)
    pd()
    rt(90)
    fd(x*2)
    rt(153.5)
    fd(x*2.25)
    go(home)

def P(x):
    home = pos()
    fd(x/2)
    circle(-x/2,180)
    fd(x/2)
    rt(90)
    fd(x)
    bk(2*x)
    go(home)

def R(x):
    home = pos()
    fd(x/2)
    circle(-x/2,180)
    lt(115)
    fd(x*1.11)
    bk(x*1.11)
    rt(115)
    fd(x/2)
    rt(90)
    fd(x)
    bk(2*x)
    go(home)

def T(x):
    home = pos()
    fd(x)
    bk(x/2)
    rt(90)
    fd(x*2)
    go(home)

def V(x):
    home = pos()
    rt(77)
    fd(x*2)
    lt(156)
    fd(x*2)
    go(home)

def X(x):
    home = pos()
    rt(65)
    fd(2.25*x)
    bk(x*2.25)
    go(home)
    pu()
    fd(x)
    pd()
    rt(180-65)
    fd(2.25*x)
    go(home)

def Z(x):
    home = pos()
    fd(x)
    rt(120)
    fd(2*x)
    lt(120)
    fd(x)
    go(home)

def A(x):
    for i in range(4):
        fd(x)
        rt(90)
    movefd(x)
    rt(90)
    fd(2 * x)
    rt(90)
    movefd(x)
    rt(90)
    fd(2 * x)
    rt(90)


def C(x):
    start = pos()
    fd(x)
    fd(-x)
    rt(90)
    fd(2 * x)
    lt(90)
    fd(x)
    go(start)


def E(x):
    start = pos()
    for i in range(2):
        fd(x)
        fd(-x)
        rt(90)
        fd(x)
        lt(90)
    fd(x)
    go(start)


def G(x):
    start = pos()
    fd(x)
    fd(-x)
    rt(90)
    fd(2 * x)
    for i in range(2):
        lt(90)
        fd(x)
    lt(90)
    fd(.5 * x)
    go(start)


def I(x):
    start = pos()
    fd(x)
    fd(-.5 * x)
    rt(90)
    fd(2 * x)
    rt(90)
    fd(.5 * x)
    fd(-x)
    go(start)


def K(x):
    start = pos()
    rt(90)
    fd(x)
    lt(135)
    for i in range(2):
        fd(sqrt(2) * x)
        fd(-sqrt(2) * x)
        rt(90)
    lt(45)
    fd(x)
    go(start)


def M(x):
    start = pos()
    degreex = degrees(atan(.5))
    rt(90)
    fd(2 * x)
    go(start)
    rt(90 - degreex)
    fd(sqrt(1.25) * x)
    setheading(360)
    lt(90 - degreex)
    fd(sqrt(1.25) * x)
    setheading(270)
    fd(2 * x)
    go(start)


def O(x):
    movefd(.5 * x)
    for i in range(2):
        circle(-.5 * x, 90)
        fd(x)
        circle(-.5 * x, 90)
    movefd(-.5 * x)


def Q(x):
    movefd(.5 * x)
    circle(-.5 * x, 90)
    fd(x)
    circle(-.5 * x, 45)
    lt(90)
    fd(.25 * x)
    fd(-.5 * x)
    fd(.25 * x)
    rt(90)
    circle(-.5 * x, 45)
    circle(-.5 * x, 90)
    fd(x)
    circle(-.5 * x, 90)
    movefd(-.5 * x)


def S(x):
    start = pos()
    movefd(x)
    fd(-.5 * x)
    circle(-.5 * x, -180)
    setheading(360)
    circle(-.5 * x, 180)
    fd(.5 * x)
    go(start)


def U(x):
    start = pos()
    rt(90)
    fd(1.5 * x)
    circle(.5 * x, 180)
    fd(1.5 * x)
    go(start)


def W(x):
    start = pos()
    rt(90)
    fd(2 * x)
    degreex = degrees(atan(.5))
    rt(180 + degreex)
    fd(sqrt(1.25) * x)
    setheading(270)
    lt(degreex)
    fd(sqrt(1.25) * x)
    setheading(90)
    fd(2 * x)
    go(start)

def Y(x):
    start = pos()
    rt(90)
    fd(.5 * x)
    circle(.5 * x, 180)
    fd(.5 * x)
    setheading(270)
    fd(1.5 * x)
    circle(-.5 * x, 180)
    go(start)

#for .
def period(x):
    home = pos()
    rt(90)
    movefd(2*x)
    for i in range(4):
        fd(x/10)
        rt(90)
    go(home)
# for ,
def comma(x):
    home = pos()
    rt(90)
    fd(2*x)
    lt(45)
    fd(x/10)
    go(home)
# for '
def apos(x):
    home = pos()
    rt(45)
    fd(x/10)
    go(home)
#for ?
def question(x):
    home = pos()
    rt(90)
    movefd(x)
    circle(x/2,-270)
    rt(90)
    fd(9*x/10)
    movefd(x/10)
    for i in range(4):
        fd(x/10)
        rt(90)
    go(home)
#for !
def eccpoint(x):
    rt(90)
    fd(2*x)
    movefd(x / 10)
    for i in range(4):
        fd(x / 10)
        rt(90)
    go(home)
#moves turtle so whole sentence fits
def moveto(x,y):
    pu()
    goto(x,y)
    pd()