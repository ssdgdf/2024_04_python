import sqlite3

connection = sqlite3.connect('test2.db')
cursor = connection.cursor()

sql2 = """
INSERT INTO BOOKS('id','title','author','published_year','in_stock')
VALUES (1,'반지의 제왕','톨킨','1999년',1);


"""

cursor.execute(sql2)
connection.commit()
connection.close()