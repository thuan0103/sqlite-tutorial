import sqlite3

conn = sqlite3.connect("customer.db")

c = conn.cursor()
c.execute(" DELETE FROM customers WHERE rowid = 4")
conn.commit()
conn.close()