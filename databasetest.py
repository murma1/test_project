import sqlite3

connection = sqlite3.connect('users.sqlite')
cursor = connection.cursor()
result = cursor.execute('''
DELETE FROM items
WHERE price = 15000
''')
connection.commit()
