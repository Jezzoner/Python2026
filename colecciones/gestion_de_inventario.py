print("="*40)
print("*"*5, "GESTION DE INVENTARIO", "*"*5)
print("="*40)

inventario = []


cant_agregar = int(input("Cuantos productos deseas agregar al inventario: "))

for i in range(cant_agregar):
   print(f"Proporciona los valores del producto {i+1}")
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

print(inventario)

busqueda_id = int(input("Ingresa el ID del producto a buscar: "))
busqueda = inventario[busqueda_id] 

print(f'''Informacion del producto encontrado:\n
      id: {busqueda_id}      
      Nombre: {busqueda['nombre'].capitalize()}
      Precio: ${busqueda['precio']:.2f}
      Cantidad: {busqueda['cantidad']}
      ''')

print("-"*3, "Inventario Detallado Actualizado", "-"*3)
for producto in inventario:
   print(f'''
      id: {producto['id']}
      Nombre: {producto['nombre'].capitalize()}
      Precio: ${producto['precio']:.2f}
      Cantidad: {producto['cantidad']}
      ''')  