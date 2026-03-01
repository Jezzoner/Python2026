from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
   SELECCIONAR  = 'SELECT * FROM cliente ORDER BY id'
   INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
   ACTUALIZAR = 'UPDATE cliente SET  nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
   ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

   @classmethod
   def seleccionar(cls):
      conexion = None
      try:
         conexion = Conexion.obtener_conexion()
         cursor = conexion.cursor()
         cursor.execute(cls.SELECCIONAR)
         registros = cursor.fetchall()
         #Mapeo de clase-tabla cliente
         clientes = []
         for registro in registros:
            cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
            clientes.append(cliente)
         return clientes
      except Exception as e:
         print(f"Ocurrio un error al seleccionar clientes: {e}")
      finally:
         if conexion is not None:
            cursor.close()
            Conexion.liberar_conexion(conexion)

   @classmethod
   def insertar(cls, cliente):
      conexion = None
      try:
         conexion = Conexion.obtener_conexion()
         cursor = conexion.cursor()
         valores = (cliente.nombre, cliente.apellido, cliente.membresia)
         cursor.execute(cls.INSERTAR, valores)
         conexion.commit() #guardar los datos en la db
         print(f'\nSe ha agregado el nuevo registro a la DB: {valores}')
         return cursor.rowcount #contador de registros
      except Exception as e:
         print(f"Ocurrio un error al insertar un cliente: {e}")
      finally:
         if conexion is not None:
            cursor.close()
            Conexion.liberar_conexion(conexion)      

   @classmethod
   def actualizar(cls, cliente):
      conexion = None
      try:
         conexion = Conexion.obtener_conexion()
         cursor = conexion.cursor()
         valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
         cursor.execute(cls.ACTUALIZAR, valores)
         conexion.commit() #guardar los datos en la db
         print(f'Se ha actualizado el registro a la DB: {valores}')
         return cursor.rowcount #contador de registros
      except Exception as e:
         print(f"Ocurrio un error al actualizar un cliente: {e}")
      finally:
         if conexion is not None:
            cursor.close()
            Conexion.liberar_conexion(conexion)    

   @classmethod
   def eliminar(cls, cliente):
      conexion = None
      try:
         conexion = Conexion.obtener_conexion()
         cursor = conexion.cursor()
         valores = (cliente.id, )
         cursor.execute(cls.ELIMINAR, valores)
         conexion.commit() #guardar los datos en la db
         print(f'Se ha eliminado el registro a la DB: {valores}')
         return cursor.rowcount #contador de registros
      except Exception as e:
         print(f"Ocurrio un error al eliminar un cliente: {e}")
      finally:
         if conexion is not None:
            cursor.close()
            Conexion.liberar_conexion(conexion)    

if __name__ == '__main__':
   #insertar cliente
   #cliente1 = Cliente(nombre='Alejandra', apellido='Tellez', membresia=300)
   #clientes_insertados = ClienteDAO.insertar(cliente1)
   #print(f"Clientes insertados: {clientes_insertados}")

   #actualizar cliente
   #cliente_actualizar = Cliente(3, 'Alexa', 'Tellez', 400)
   #clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
   #print(f"Cliente actualizado: {clientes_actualizados}")

   #eliminar cliente
   #cliente_eliminar = Cliente(id=3)
   #clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
   #print(f"Clientes eliminados: {clientes_eliminados}")

   #seleccionar los clientes
   clientes = ClienteDAO.seleccionar()
   for cliente in clientes:
      print(cliente)