import sqlite3 #adds the dependency
con = sqlite3.connect("tutorial.db") #creates the database and connects to it

cur = con.cursor()#creates a cursor to execute SQL statements and fetch results from queries
cur.execute("CREATE TABLE movie(title, year, score)") #- executes the SQL command in the parenthesis

res = cur.execute("SELECT name FROM sqlite_master")#result of the query
res.fetchone()#fetches the row

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit() #when using 'INSERT' it starts a transaction that needs to be committed before saving changes in the datbase itself

res = cur.execute("SELECT score FROM movie")

res.fetchall() #fetches all resulting rows

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data) #uses ? placeholders to protect code from an sql injection attack
con.commit()

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):

    print(row)