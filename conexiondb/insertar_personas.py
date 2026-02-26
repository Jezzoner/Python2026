import mysql.connector

personas_db = mysql.connector.connect(
   host='localhost', #127.0.0.1
   user='root',
   password='root',
   database='personas_db'
)

cursor = personas_db.cursor()
sentencia_sql = 'insert into personas(nombre, apellido, edad) values(%s, %s, %s)'
valores = ('Victor', 'Ramos', 46)
cursor.execute(sentencia_sql, valores)
personas_db.commit() #guardar los datos en la db
print(f'Se ha agregado el nuevo registro a la DB: {valores}')
cursor.close()
personas_db.close()