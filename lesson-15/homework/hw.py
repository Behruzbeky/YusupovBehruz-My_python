import sqlite3

conn=sqlite3.connect('my_database.db')
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,       
    Age INTEGER
)''')
conn.commit()       
conn.close()

print("Database and table created successfully.")

roster_data= [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]



import sqlite3
conn=sqlite3.connect('my_database.db')
cursor=conn.cursor()

cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")
conn.commit()
print("Data updated successfully.")

conn.close()




import sqlite3
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()
cursor.execute("""
select name, age from Roster
where species = 'Bajoran'
""")
results = cursor.fetchall()
print("Bajoran Species:")
for row in results:     
    print(f"Name': {row[0]}, Age: {row[1]}")
conn.commit()
conn.close()            



