# -*- coding: utf-8 -*-
"""
Anne Harding, 28/02/2019
GEOG5790 - Practical 5 (SQLite)
PART ONE - Creating Database
Script to connect to sqlite database, create a table and write data to it.
"""

# Import modules:
import sqlite3

# Connect to database:
conn = sqlite3.connect('database.sqlite')

# Get a cursor from connection to interact with database:
c = conn.cursor()

# Execute SQL to create a table: - note that this line can only run once!
# c.execute("CREATE TABLE Results (address text, burglaries integer)")

# Execute SQl to insert data:
c.execute("INSERT INTO Results VALUES ('Queen Vic',2)")

# Commit changes:
conn.commit()

# Close connection:
conn.close()