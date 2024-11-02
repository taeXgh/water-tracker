#---------------------------------------------------------------------
# Water Tracker Application
#
#
# Author: Thalia Edwards         Date: 11/2/2024 
#
# Purpose: Linux Mint Desklet to track your water intake
#---------------------------------------------------------------------
import random

greetings = {1 : "Hey thirsty! Let's track your water intake!", 
             2 : "You've been drinking, you've been drinking?",
             3 : "How much have you had to drink tonight?",
             4 : "Look at you drinking water!\nHow much have you had?",
             5 : "You know the drill, how much water intake do you want to log?"}

motivation = {1 : "Good job!", 
             2 : "You're doing amazing sweetie!",
             3 : "Yay! Good work :)",
             4 : "WOOOOO you're killing it",
             5 : "You'll reach your goal in no time ;)"}

messageChoice = random.randrange(1, 6)
more = 'y'
totalIntake = []

def IntakeLog():
    while True:
        try:
            intakeAmt = int(input(f'{greetings.get(messageChoice)}\nWater Amount in mL: '))
            totalIntake.append(intakeAmt)
            print(f'{motivation.get(messageChoice)}')
            selection = input('Do you want to log more water today? (y/n)')
            if selection in more:
                continue
            else:
                finalIntake = sum(totalIntake)
                print(f'Your total intake for today is {finalIntake} so far!')
                return False
                break
                
            if type(intakeAmt) is not int:
                raise TypeError
        except:
            print("\nSomething went wrong, try again\n")
    
    

# Global code starts here ----------------------------------------------------------------------------------------------------------------------\

IntakeLog()