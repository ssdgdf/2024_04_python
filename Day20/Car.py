import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

sql = """
CREATE TABLE RESERVATION(
    reverse_number INTEGER PRIMARY KEY ,
    reverse_carnumber INTEGER,
    reverse_startday TEXT
)

"""
cursor.execute(sql)
connection.commit()
connection.close()


# import sqlite3
#
# connection = sqlite3.connect('test.db')
# cursor = connection.cursor()
#
# sql = """
#     INSERT IN TO CAR ('car_number','car_name','car_color','car_company')
#     VALUES ('1234','테슬라','검정색','테슬라');
# """
# cursor.execute(sql)
# connection.commit()
# connection.close()

# import sqlite3
#
# connection = sqlite3.connect('test2.db')
# cursor = connection.cursor()
#
# sql2 = """
#     INSERT IN TO CAR ('id','name','address','number')
#     VALUES ('asd','배준식','서울시','01012345678');
# """
# cursor.execute(sql2)
# connection.commit()
# connection.close()

# CREATE TABLE MEMBERS(
#     id INTEGER PRIMARY KEY ,
#     name TEXT,
#     address TEXT,
#     number INTEGER
# ),
#
# CREATE TABLE RESERVATION(
#     reverse_number INTEGER PRIMARY KEY ,
#     reverse_carnumber INTEGER,
#     reverse_startday TEXT
# )