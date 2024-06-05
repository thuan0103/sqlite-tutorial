import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

many_customer = [
    ('Wes','Brow','wes@brown.com'),
    ('Steph','Kuewa','steph@kuewa.com'),
    ('Dan','Pas','dan@pas.com')
    ]

#c.execute("INSERT INTO customers VALUES('John','Elder','john@codemy.com')")

c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customer)

conn.commit()
conn.close()