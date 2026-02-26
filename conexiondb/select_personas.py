import mysql.connector

personas_db = mysql.connector.connect(
   host='localhost', #127.0.0.1
   user='root',
   password='root',
   database='personas_db'
)

#ejecutar sentencia select
cursor = personas_db.cursor()
cursor.execute('select * from personas');
resultado = cursor.fetchall()

for persona in resultado:
   print(persona)

cursor.close()
personas_db.close()