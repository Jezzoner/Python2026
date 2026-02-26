import mysql.connector

personas_db = mysql.connector.connect(
   host='localhost', #127.0.0.1
   user='root',
   password='root',
   database='personas_db'
)

cursor = personas_db.cursor()
sentencia_sql = 'update personas set nombre=%s, apellido=%s, edad=%s where id=%s'
valores = ('Victoria', 'Flores', 45, 5)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print(f"Se ha modificado la informacion: {valores}")
cursor.close()
personas_db.close()