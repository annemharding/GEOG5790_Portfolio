# -*- coding: utf-8 -*-
"""
Anne Harding, 28/02/2019
GEOG5790 - Practical 5 (SQLite)
PART TWO - Reading Database
Script to conect to sqlite database and read rows from it.
"""

# Import modules:
import sqlite3

# Connect to database:
conn = sqlite3.connect('database.sqlite')

# Get a cursor:
c = conn.cursor()

# Read table rows and print the first value in each row:
for row in c.execute('SELECT * FROM Results ORDER BY burglaries'):
    # print(row[0])
    # print(u'{0}, {1}'.format(row[0], row[1]))
    print(u'{1} burglary(ies) have happened at {0}.'.format(row[0], row[1]))

# Close connection:
conn.close()