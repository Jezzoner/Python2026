from cliente_dao import ClienteDAO
from cliente import Cliente
from art import text2art

title = text2art("Zona Fit (Gym)")
print(title)

opcion = None
while opcion != 5:
   print(f'''Menu:
         1. Listar clientes
         2. Agregar cliente
         3. Modificar cliente
         4. Eliminar cliente
         5. Salir''')
   opcion = int(input("Escoge una opcion (1-5): "))
   if opcion == 1:
      clientes = ClienteDAO.seleccionar()
      print("\n", "=" * 16, "Listado de clientes", "=" * 16)
      for cliente in clientes:
         print(cliente)
   elif opcion == 2:
      nombre_var = input("Escribe el nombre: ")
      apellido_var = input("Escribe el apellido: ")
      membresia_var = int(input("Escribe la membresia: "))
      cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
      cliente_insertado = ClienteDAO.insertar(cliente)
      print(f"Cliente insertado: {cliente_insertado}\n")
   elif opcion == 3:
      id_cliente_var = int(input("Escribe el ID del cliente a modificar: "))
      nombre_var = input("Escribe el nombre: ")
      apellido_var = input("Escribe el apellido: ")
      membresia_var = int(input("Escribe la membresia: "))
      cliente = Cliente(id_cliente_var, nombre_var, apellido_var, membresia_var)
      cliente_actualizado = ClienteDAO.actualizar(cliente)
      print(f"Cliente actualizado: {cliente_actualizado}")
   elif opcion == 4:
      id_cliente_var = int(input("Escribe el 'ID' del cliente a eliminar: "))
      cliente = Cliente(id=id_cliente_var)
      cliente_eliminado = ClienteDAO.eliminar(cliente)
      print(f"Cliente eliminado: {cliente_eliminado}")
   elif opcion == 5:
      print("Muchas gracias...")
   else:
      print("Opcion invalida, intente de nuevo (1-4)")