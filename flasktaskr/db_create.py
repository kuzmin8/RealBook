import sqlite3

from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    c.execute(""" CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGET NOT NULL, status INTEGET NOT NULL) """)
    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES ("Finish this tutorial" , "03/25/2023", 10, 1)'
    )
    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES ("Finish Real Python Course 2 ", "03/25/2025", 10, 1)'

    )
