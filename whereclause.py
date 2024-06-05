import sqlite3

conn = sqlite3.connect("customer.db")

c = conn.cursor()

# Tìm tất cả các bản ghi mà last_name chính xác là 'Dan'
c.execute("SELECT * FROM customers WHERE first_name = 'Dan'")

items = c.fetchall()
print(items)

conn.close()
