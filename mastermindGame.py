#Kayla Washington PD-3
#Tasks attempted 1 2 3 4 5A 5B
from random import *

# prints guidlines
print("Welcome to Mastermind!")
print("The computer will pick different numbers. You will then have a certain number of attempts to try and guess all numbers.")
print("The computer, after each try the computer will tell you if you guessed the correct number and if they are in the correct place.")
print("Enter numbers with spaces between them like this: 1 2 3 4")

print("Let's play!")

comprange = ["1-6", "1-7", "1-8", "1-9", "1-10"] #range of numbers

for i in range(len(comprange)): #prints menu for the range
    print(i+1,". ",comprange[i])

userrange = int(input("Pick a range from which you want the numbers to vary: ")) #user picks range of numbers

k= 0 #variable for range

if(userrange == 1): #if user picks range 1-6
    k = 6
elif(userrange == 2): #if user picks range 1-7
    k = 7
elif(userrange == 3): #if user picks range 1-8
    k = 8
elif(userrange == 4): #if user picks range 1-9
    k = 9
elif(userrange == 5): #if user picks range 1-10
    k = 10
else: #if user picks something out of range
    userrange = int(input("Please pick within our range"))

numofnum = ["4", "5", "6", "7", "8"] #how many numbers to guess
w = 0 #condition for the while
for i in range(len(numofnum)): #prints menu for length of numbers
    print(i+1,". ", numofnum[i])
p = int(input("How many numbers do you want? "))
if(p == 1): #if user picks 4
    w = 4
elif(p == 2): #if user picks 5
    w = 5
elif(p == 3): #if user picks 6
    w = 6
elif(p == 4): #if user picks 7
    w = 7
elif(p == 5): #if user picks 8
    w = 8

cpusolution = [] #solution
n = 0

Modes = ["Easy", "Medium", "Hard"] #different levels

for i in range(len(Modes)): #print menu of modes
    print(i+1, Modes[i])

mods = int(input("Pick a mode: ")) #user picks a mode
#mode manipulates the number of attempts the user is allowed
if(mods == 1): #if user picks easy
    n = 12
elif(mods== 2): #if user picks medium
    n = 8
elif(mods == 3): #if user picks hard
    n = 4
for i in range(0,w): #picks random integers for the answer
    cpusolution.append(randint(1,k))

track = [] #users guesses

cguesses = 0 #correct guesses

cplaces = 0 #correct places

win = 0

print("You chose: ","Range = ", comprange[userrange-1], "Mode = ", Modes[mods-1], "# of numbers = ", ) #prints how the game was chosen
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~LET'S PLAY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")#border
while(n > 0 and win == 0): #continues if the user hasn't won or lost
    cplaces = 0 #resets the correct places for user input
    cguesses = 0 #resets the correct guesses for user input
    n = n - 1 #number of tries
    userinput = ((input("Please enter digits: ")).split()) #splits user input into seperate indicies of the list
    for i in range(len(userinput)): #this checks to make sure the user puts numbers only
        if(userinput[i].isdigit()== False):
            print("You have to use numbers!!!!!!")
            userinput = ((input("Please enter NUMBERS: ")).split()) #user  picks numbers again
    for i in range(len(userinput)): #changes user input from string to integer
        userinput[i] = int(userinput[i])
    track.append(userinput) #keeps track of all guesses
    if(len(userinput != cpusolution)): #makes sure that the user inputs the proper number of numbers
        userinput = ((input("Please enter the correct number of digits: ")))
        for i in range(len(userinput)): #changes user input from string to integer
            userinput[i] = int(userinput[i])
    for i in range(len(cpusolution)):
        if(userinput[i] in cpusolution): #if the user has a correct guess but wrong place
            cguesses += 1
        if (userinput[i] == cpusolution[i]): #if the user has the correct guess in the correct place
            cplaces += 1

    if(cguesses == w and cplaces == w): #if the user guesses correctly
        win = 1

    print("Correct guesses: ",cguesses,"Correct places: ",cplaces) #prints result

    print("Attemps: ",track) #prints previous guesses

    print("Number of tries left: ", n) #prints number of attempts left

if(n == 0): #if the player runs out of tries
    print("YOU LOST!!!!!!!!LOSER")
    print("The answer was: ", cpusolution)

elif(win != 0): #if the user guesses correctly
    print("YAYYYYYYY!!!!!! You won!")
    print("The answer was: ", cpusolution)