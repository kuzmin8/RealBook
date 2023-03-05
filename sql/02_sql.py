import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO populations VALUES('New York City',\
'NY', 8400000)")
    cursor.execute("INSERT INTO populations VALUES('San Francisco', \
'CA', 8000000)")


    conn.commit()
except sqlite3.OperationalError:
    print("Oops! Something went wrong. Try again...")

conn.close()
#Same code

# with sqlite3.connect("new.db") as connection:
#     c = connection.cursor()
#     c.execute("INSERT INTO population VALUES('New York City',\
#      'NY', 8400000)")
#     c.execute("INSERT INTO population VALUES('San Francisco', \
#     'CA', 8000000)")