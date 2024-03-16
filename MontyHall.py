# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 09:40:24 2024

@author: payta
"""
"""
Psuedocode
1. Our program needs two inputs, trails and strategy. I will represent trails with an int and strategy with a bool
2. Our function will have to run a loop where it will do the following
    a. create a list with 3 elements(these will be our doors)
    b. randomly assign one of those doors to have a car behind it
    c. randomly select a door to choose
    d. if the strategy is switch, then we locate both of the goat doors and randomly reveal an unchosen one
       then switch to the remaining door
    e. if the strategy is no switch, then just reveal if the correct door was chosen
    f. keep track of how many were successful and find that percentage
"""


import random as rd

def MontyHallDoor(trails = 10, switch = True):
    
    winner = 0
    
    for i in range(trails):
        doors = ["Goat", "Goat", "Goat"]
        WinDoor = rd.randint(0,2)
        doors[WinDoor] = "Car"
        
        choice = rd.randint(0,2)
        
        if (switch == True):
            
            check = False
            while (check == False):
                reveal = rd.randint(0,2)
                if (reveal != choice and doors[reveal] != "Car"):
                    check = True
                    
            if (choice != 0 and reveal != 0):
                newChoice = 0
            elif (choice != 1 and reveal != 1):
                newChoice = 1
            else:
                newChoice = 2
                
            if (doors[newChoice] == "Car"):
                winner += 1
            
        else:
            if (doors[choice] == "Car"):
                winner += 1
    winRate = winner / trails
    return winRate

#Here are some test lines listed below
"""
winSmallSwitch = MontyHallDoor(10, True)
winLargeSwitch = MontyHallDoor(1000, True)
winVLargeSwitch = MontyHallDoor(1000000, True)
winSmallNoSwitch = MontyHallDoor(10, False)
winLargeNoSwitch = MontyHallDoor(1000, False)
winVLargeNoSwitch = MontyHallDoor(1000000, False)

print("Small Switch: " + str(winSmallSwitch))
print("Large Switch: " + str(winLargeSwitch))
print("Very Large Switch: " + str(winVLargeSwitch))
print("Small No Switch: " + str(winSmallNoSwitch))
print("Large No Switch: " + str(winLargeNoSwitch))
print("Very Large No Switch: " + str(winVLargeNoSwitch))
"""