from turtle import *
from math import *
colormode(255) #changes mode so it reads the r, g, b format
speed(0)
#set variables relative to A
A = int(input("Enter selected hoist: ")) #user inputs the hoist for the flag
B = A*(1.9) #fly of the flag
D = A*(0.76) #FLy of the union
C = A*(7/13) #hoist of the union
# function for moving to specific points
def moveto(x,y):
    pu()
    goto(x,y)
    pd()
moveto(-B/2,A/2)
#draws shape of the fag
def starting(a,b):
    for i in range(2):
        fd(b)
        rt(90)
        fd(a)
        rt(90)
starting(A,B)
L = A*(1/13)
#draws and fills the stripes on the flag
def lines(a,b):
    for j in range(13):
        if(j%2==0):
            fillcolor(178, 34, 52)
        elif(j%2 != 0):
            fillcolor(255, 255, 255)
        begin_fill()
        for i in range(2):
            fd(a)
            rt(90)
            fd(b)
            rt(90)
        end_fill()
        moveto(xcor(),ycor()-L)
# dimensions of the stripes
lines(B,L)
moveto(xcor(),ycor()+A)
fillcolor(60, 59, 110)
#function for the union of the flag
def bluerectangle(x,y):
    begin_fill()
    for i in range(2):
        fd(x)
        rt(90)
        fd(y)
        rt(90)
    end_fill()
bluerectangle(D,C)
r= (A*(0.0616))/2 #radius of star
E = A*(0.054)
H = A*(0.063)
moveto((-B/2)+(H),(A/2)-(E*.5)) #where the first star will place itself


s = r * sin(radians(36)) / sin(radians(126))
rt(90-18)
color(255,255,255)
# function for stars to print out horizontally
def stars(x):
    for i in range(x):
        fillcolor(255, 255, 255)
        begin_fill()
        for i in range(5):
            fd(s)
            lt(72)
            fd(s)
            rt(144)
        end_fill()
        moveto(xcor()+ (H*2),ycor()) #distance between each star

n=1.5 #variable to change the ycor()
#loop for changing star rows
for i in range(4):
    stars(6)
    moveto((-B/2)+(H*2),(A/2)-(E*n))
    stars(5)
    n+=1
    moveto((-B/2)+(H),(A/2)-(E*n))
    n+=1
stars(6)
exitonclick()