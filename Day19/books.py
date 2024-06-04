import sqlite3

connection = sqlite3.connect('test2.db')
cursor = connection.cursor()

sql2 = """
CREATE TABLE BOOKS(
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    published_year INTEGER,
    in_stock BOOLEAN

)
"""

cursor.execute(sql2)
connection.commit()
connection.close()