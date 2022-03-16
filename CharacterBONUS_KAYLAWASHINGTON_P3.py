#Kayla Washington PD-3

from turtle import *
from math import *
from CharacterBONUS_Lib_KAYLAWASHINGTON_P3 import *
#user inputs word/sentence
word = input("Enter a word/sentence: ")
# function for the size of the user's word/sentence
def size(x):
    moveto(-500, 0)
    #goes through each character in the word/sentence
    for i in word:
        if(i == "a" or i == "A"):
            A(x)
        elif(i == "b" or i == "B"):
            B(x)
        elif(i == "c" or i == "C"):
            C(x)
        elif(i == "d" or i == "D"):
            D(x)
        elif(i == "e" or i == "E"):
            E(x)
        elif(i == "f" or i == "F"):
            F(x)
        elif(i == "g" or i == "G"):
            G(x)
        elif(i == "h" or i == "H"):
            H(x)
        elif(i == "i" or i == "I"):
            I(x)
        elif(i == "j" or i == "J"):
            J(x)
        elif(i == "k" or i == "K"):
            K(x)
        elif(i == "l" or i == "L"):
            L(x)
        elif(i == "m" or i == "M"):
            M(x)
        elif(i == "n" or i == "N"):
            N(x)
        elif(i == "o" or i == "O"):
            O(x)
        elif(i == "p" or i == "P"):
            P(x)
        elif(i == "q" or i == "Q"):
            Q(x)
        elif(i == "r" or i == "R"):
            R(x)
        elif(i == "s" or i == "S"):
            S(x)
        elif(i == "t" or i == "T"):
            T(x)
        elif(i == "u" or i == "U"):
            U(x)
        elif(i == "v" or i == "V"):
            V(x)
        elif(i == "w" or i == "W"):
            W(x)
        elif(i == "x" or i == "X"):
            X(x)
        elif(i == "y" or i == "Y"):
            Y(x)
        elif(i == "z" or i == "Z"):
            Z(x)
        elif(i == " "):
            space(x)
        elif(i == "."):
            period(x)
        elif(i == "?"):
            question(x)
        elif(i == "!"):
            eccpoint(x)
        elif(i == "'"):
            apos(x)
        space(x)
#user chooses the size of the words
size(int(input("Enter the size of your choosing: ")))
exitonclick()