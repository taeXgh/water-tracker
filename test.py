import sqlite3 #adds the dependency

con = sqlite3.connect("tutorial.db") #creates the database and connects to it

cur = con.cursor()#creates a cursor to execute SQL statements and fetch results from queries
cur.execute("CREATE TABLE movie(title, year, score)")

res = cur.execute("SELECT name FROM sqlite_master")

res.fetchone()