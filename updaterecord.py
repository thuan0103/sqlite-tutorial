import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()
#update record
c.execute("""
    UPDATE customers SET first_name = 'Bod'
    WHERE last_name = 'Elder'
""")
conn.commit()
c.execute("SELECT * FROM customers")
print(c.fetchall())
conn.close()