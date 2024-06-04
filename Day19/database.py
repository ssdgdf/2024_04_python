
import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

sql = """
CREATE TABLE COFFEE(
    id INTEGER PRIMARY KEY,
    coffeename TEXT,
    coffeeprice INTEGER,
    coffeeKcal INTEGER
)
"""

cursor.execute(sql)
connection.commit()
connection.close()