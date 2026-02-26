import mysql.connector

personas_db = mysql.connector.connect(
   host='localhost', #127.0.0.1
   user='root',
   password='root',
   database='personas_db'
)

cursor = personas_db.cursor()
sentencia = 'delete from personas where id = %s'
valores = (5, )
cursor.execute(sentencia, valores)
personas_db.commit()
print(f"Eliminado correctamente el registro: {valores}")
cursor.close()
personas_db.close()
