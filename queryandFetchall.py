import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()
#query database
c.execute("SELECT * FROM customers")
# print(c.fetchone()[0])
# c.fetchmany(3)
items = c.fetchall()
# print(items)
for item in items:
    print(item[0])
#format your results
conn.commit()
conn.close()