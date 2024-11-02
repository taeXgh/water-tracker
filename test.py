""" import sqlite3 #adds the dependency
con = sqlite3.connect("intakelogs.db") #creates the database and connects to it

cur = con.cursor()#creates a cursor to execute SQL statements and fetch results from queries
cur.execute("CREATE TABLE IF NOT EXISTS intakelogs(dateTime, total)") #- executes the SQL command in the parenthesis

res = cur.execute("SELECT name FROM sqlite_master")#result of the query

data = [
    ("10/24/24", 16),
    ("10/31/24", 8),
    ("11/2/24", 12),
]

cur.executemany("INSERT INTO intakelogs VALUES(?, ?)", data) #uses ? placeholders to protect code from an sql injection attack
con.commit()#when using 'INSERT' it starts a transaction that needs to be committed before saving changes in the datbase itself

res.fetchall() #fetches all resulting rows

for row in cur.execute("SELECT total FROM intakelogs ORDER BY dateTime"):
    print(row) """
#-------------------------------------------------------------------------------------------------------------------------------------------------------
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
            intakeAmt = int(input(f'{greetings.get(messageChoice)}\nWater Amount in mL: ')) #initial greeting 
            totalIntake.append(intakeAmt) #adds every entry to the totalIntake list
            print(f'{motivation.get(messageChoice)}')#selects a random motivational message to encourage the user
            selection = input('Do you want to log more water today? (y/n)')#determines whether the program ends or logs another entry
            if selection in more:
                continue
            else:
                finalIntake = sum(totalIntake)
                print(f'Your total intake for today is {finalIntake} ml so far!')
                return False
                break
                
            if type(intakeAmt) is not int:
                raise TypeError
        except:
            print("\nSomething went wrong, try again\n")
    
    

# Global code starts here ----------------------------------------------------------------------------------------------------------------------\

IntakeLog()