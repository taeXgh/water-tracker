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

greetingChoice = random.randrange(1, 6)
more = 'y'
totalIntake = []

def IntakeLog():
    while True:
        try:
            intakeAmt = int(input(f'{greetings.get(greetingChoice)}\nWater Amount in mL: '))
            totalIntake.append(intakeAmt)
            print(f'Wow so far your water intake is {intakeAmt} mL today!')
            selection = input('Do you want to log more water today? (y/n)')
            if selection in more:
                continue
            else:
                print(totalIntake)
                return False
                break
                
            if type(intakeAmt) is not int:
                raise TypeError
        except:
            print("\nSomething went wrong, try again\n")
    
    

# Global code starts here ----------------------------------------------------------------------------------------------------------------------\

IntakeLog()