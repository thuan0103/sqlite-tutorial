import sqlite3

conn = sqlite3.connect("customer.db")

c = conn.cursor() # create cursor

c.execute("""
    CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
)""")

#text
# null
# interger
# real
# blob

conn.commit()

# close our connection
conn.close()