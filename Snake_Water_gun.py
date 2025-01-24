'''
Rules:
1. snake + water  = snake win
2. snake + gun = gun win
3. water + gun = water win

approach:

set up the computer input which is using random module in 
    snake:1
    water:-1
    gun:0

then take input from user in str form 

then use your above logic:
    logic 1: use naive sol. 
    logic 2: use shortened method
            computer - user = -1 or 2 ---> u will loose
            computer - user = 1 or -2 ---> u will win

we will do it by both method, Let's start..... hurraaay!

'''

import random

computer_input  = random.choice([1,-1,0]) # number form

user_input = input("User Input: ") # string form

dict = {"snake":1,"water":-1,"gun":0}
revDict = {1:"snake",-1:"water",0:"gun"}

userNum = dict[user_input] # number form 

print(f"User choose: {revDict[userNum]} \nComputer choose: {revDict[computer_input]}")
if computer_input == userNum:
    print("Draw ! Try again.")
else:
    if computer_input == 1 and userNum == 0:
        print("You win, Great!")
    elif computer_input == 1 and userNum == -1:
        print("Ohhoo..., You lost this Game., Best of luck for Next Game!")
    elif computer_input == -1 and userNum == 1:
        print("You win, Great!")
    elif computer_input == 1 and userNum == 0:
        print("Ohhoo..., You lost this Game., Best of luck for Next Game!")
    elif computer_input == 0 and userNum == -1:
        print("You win, Great!")
    elif computer_input == 0 and userNum == 1:
        print("Ohhoo..., You lost this Game., Best of luck for Next Game!")
    else:
        print("Something is Wrong!, Please look into this again.")
  
# method 2 
'''
            computer - user = -1 or 2 ---> u will loose
            computer - user = 1 or -2 ---> u will win

            This is the observation u can use this code too.

'''