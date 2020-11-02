import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

create_table="CREATE TABLE IF NOT EIXSTS users (id INTEGER PRIMARY KEY, username text, assword text)"
cursor.execute(create_table)

connection.commit()
connection.close()