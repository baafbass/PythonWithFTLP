import sqlite3

print("Personal Library Database\n")

conn = sqlite3.connect('library.db')
c=conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS Books (
BookID INTEGER PRIMARY KEY,
Title TEXT,
Author TEXT,
YearPublished INTEGER,
Genre TEXT
)
''')

conn.commit()
conn.close()

conn= sqlite3.connect('library.db')
c=conn.cursor()

c.execute("INSERT INTO Books(BookID,Title,Author,YearPublished,Genre) VALUES(?,?,?,?,?)",(1,"How to win friends and influence people","Dale Carnegie",1937,"Self-Help"))
c.execute("INSERT INTO Books (BookID,Title, Author, YearPublished,Genre) VALUES (?,?,?,?,?)", (2,"To Kill a Mockingbird", "Harper Lee", 2018,"Fiction"))
c.execute("INSERT INTO Books (BookID,Title, Author, YearPublished,Genre) VALUES (?,?,?,?,?)", (3,"The Power of Now", "Ecklart Tolle", 2014,("Finance")))
c.execute("INSERT INTO Books (BookID,Title, Author, YearPublished,Genre) VALUES (?,?,?,?,?)", (4,"Man's Search for Meaning", "Beltus Lee", 1960,"Self improvement"))
c.execute("INSERT INTO Books (BookID,Title, Author, YearPublished,Genre) VALUES (?,?,?,?,?)", (5,"The Compound Effect", 'Darren Hardy', 2004,("psychology")))

conn.commit()
conn.close()

conn=sqlite3.connect('library.db')
c=conn.cursor()

c.execute("SELECT * FROM Books")

rows = c.fetchall()

for row in rows:
  print(row)

conn.close()

conn=sqlite3.connect('library.db')
c=conn.cursor()

c.execute("SELECT * FROM Books WHERE YearPublished > ?",(2000,))

rows = c.fetchall()

for row in rows:
  print(row)

conn.close()

conn=sqlite3.connect('library.db')
c=conn.cursor()

c.execute("SELECT * FROM Books WHERE Genre = ?",("Fiction",))

rows = c.fetchall()

for row in rows:
  print(row)

conn.close()

conn= sqlite3.connect('library.db')
c=conn.cursor()

c.execute("UPDATE Books SET YearPublished = ? WHERE BookID = ?",(2023,4))

conn.commit()
conn.close()

conn= sqlite3.connect('library.db')
c=conn.cursor()

c.execute("DELETE FROM Books WHERE BookID = ?",(2,))

conn.commit()
conn.close()

conn=sqlite3.connect('library.db')
c=conn.cursor()

c.execute("SELECT * FROM Books")

rows = c.fetchall()

for row in rows:
  print(row)

conn.close()

