import sqlite3

conn = sqlite3.connect('mydb.db')
print("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE student
       (sid          char(20)    NOT NULL,
       name          char(20)    NOT NULL,
       phone         char(20)    NOT NULL,
       address       char(20)    NOT NULL);''')
print("Table created successfully")
conn.commit()
conn.close()
