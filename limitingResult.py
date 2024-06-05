import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("SELECT * FROM customers LIMIT 2")
print(c.fetchall())
conn.commit()
conn.close()