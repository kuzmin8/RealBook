import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("SELECT firstname, lastname from employe")
    rows = c.fetchall()
    print(rows)
    for r in rows:
        print(r[0], r[1])

    # for row in c.execute("SELECT firstname, lastname from employe"):
    #     print(row)
