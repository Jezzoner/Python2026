print("="*50)
print("*"*5, "Sistema de Inventarios con Funciones", "*"*5)
print("="*50)

inventario = []

cant_agregar = int(input("Cuantos productos deseas agregar al inventario: "))

for i in range(cant_agregar):
   i += 1
   print(f"\nProporciona los valores del producto {i}")
   nombre = input("Nombre: ")
   precio = float(input("Precio: "))
   cantidad = int(input("Cantidad: "))
   producto = {
      'id':i,
      'nombre':nombre,
      'precio':precio,
      'cantidad':cantidad
      }
   inventario.append(producto)
id = producto['id']

print("\nIntentario inicial:",inventario, "\n")

def mostrar_inventario():
   print()
   print("-"*3, "Inventario del almacen", "-"*3)
   for producto in inventario:
      print(f'''
         ID: {producto['id']}
         Nombre: {producto['nombre'].capitalize()}
         Precio: ${producto['precio']:.2f}
         Cantidad: {producto['cantidad']}
         ''')  

def agregar_nuevo_producto():
   print(f"\nProporciona los valores del producto")
   nombre = input("Nombre: ")
   precio = float(input("Precio: "))
   cantidad = int(input("Cantidad: "))
   global id
   id += 1
   producto = {
      'id': id,
      'nombre':nombre,
      'precio':precio,
      'cantidad':cantidad
      }
   inventario.append(producto)
   print(f"\nProducto \"{producto['nombre']}\" agregado exitosamente.\n")

def buscar_producto_por_id():
   busqueda_id = int(input("\nIngresa el ID del producto a buscar: "))
   busqueda = None
   for producto in inventario:
      if producto['id'] == busqueda_id:
         busqueda = producto
         break

   if busqueda is not None:
      print(f'''\nInformacion del producto encontrado:\n
         ID: {busqueda['id']}      
         Nombre: {busqueda['nombre'].capitalize()}
         Precio: ${busqueda['precio']:.2f}
         Cantidad: {busqueda['cantidad']}
         ''')
   else:
      print(f"\nProducto con ID {busqueda_id} NO encontrado\n")

if __name__ == "__main__":
   while True:
      print('''--- Menu ---
      1. Mostrar inventario
      2. Agregar nuevo producto
      3. Buscar producto por ID
      4. Salir''')
      opcion = int(input("Proporciona una opcion (1-4): "))
      if opcion == 1:
         mostrar_inventario()
      elif opcion == 2:
         agregar_nuevo_producto()
      elif opcion == 3:
         buscar_producto_por_id()
      elif opcion == 4:
         print("Saliendo del sistema...")
         break
      else:
         print("Opcion invalida, proporciona una opcion valida")
