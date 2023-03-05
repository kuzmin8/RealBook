import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
# open the csv file and assign it to a variable
    employees = csv.reader(open("employees.csv"))
# create a new table called employees
    c.execute("CREATE TABLE employe(firstname TEXT, lastname TEXT)")
# insert data into table
    c.executemany("INSERT INTO employe(firstname, lastname) values (?, ?)", employees)
