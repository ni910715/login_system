import sqlite3

conn = sqlite3.connect('Account.db')
mycursor = conn.cursor()


# mycursor.execute("CREATE TABLE Account(userId text PRIMARY KEY, name text, company text, number text)")
# conn.commit()

mycursor.execute("SELECT * FROM Account")

values = mycursor.fetchall()

for value in values:
    print(f"{value[0]} {value[1]} {value[2]} {value[3]}")
    
conn.close()