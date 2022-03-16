from turtle import *
from Digits_Lib_KAYLAWASHINGTON_P3 import *
#user chooses their numbers
userinput = (input("Please enter digits: "))
#function for the size of the #'s
def size(x):
    #identifies the different numbers the user choosese
    for i in userinput:
        if (i == "0"):
            zero(x)
        elif (i == "1"):
            one(x)
        elif (i == "2"):
            two(x)
        elif (i == "3"):
            three(x)
        elif (i == "4"):
            four(x)
        elif (i == "5"):
            five(x)
        elif (i == "6"):
            six(x)
        elif (i == "7"):
            seven(x)
        elif (i == "8"):
            eight(x)
        elif (i == "9"):
            nine(x)
        space(x)
#user chooses the size
size(int(input("Please choose the size you want: ")))


exitonclick()