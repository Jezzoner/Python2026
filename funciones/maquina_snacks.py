print("="*40)
print("*"*5, "Maquina de Snacks", "*"*5)
print("="*40,"\n")

snacks = [
   {'id': 1, 'nombre': 'Papas', 'precio': 30},
   {'id': 2, 'nombre': 'Refresco', 'precio': 50},
   {'id': 3, 'nombre': 'Sandwich', 'precio': 120}
]
productos = []
id = (snacks[-1].get('id'))

#Opcion 1
def mostrar_snacks():
   print()
   print("-"*3, "Snack Disponibles", "-"*3)
   for snack in snacks:
      print(f'''
   ID: {snack.get('id')}
   Nombre: {snack.get('nombre')}
   Precio: ${snack.get('precio')}
   ''')  

def agregar_snack():
   global id
   id += 1
   nombre = input("Nombre del Snack: ")
   precio = int(input("Precio del Snack: "))
   snack = {
      'id':id,
      'nombre':nombre,
      'precio':precio
   }
   snacks.append(snack)
   print(snacks)


#Busqueda de Snack por id
def busqueda_snack(id_buscar):
   for snack in snacks:
      if snack.get('id') == id_buscar:
         return snack
   return None

#Opcion 2
def comprar_snacks():
   mostrar_snacks()
   snack_id = int(input("\nQue Snack quieres comprar (ID): "))
   snack_encontrado = busqueda_snack(snack_id)
   if snack_encontrado is not None:
      productos.append(snack_encontrado)
      print(f"\nSnack agregado: {snack_encontrado.get('nombre')}\n")   
   else:  
      print(f"\nSnack NO encontrado con ID: {snack_id}\n")

#Opcion 3
def mostrar_ticket():
   print()
   print("*"*6, "Ticket de Venta", "*"*6,"\n")
   total = 0
   for producto in productos:
      print(f"- {producto.get('nombre'):<15} ... ${producto.get('precio')}")
      total += producto.get('precio')
   print("-" * 30)
   print(f"TOTAL A PAGAR:        ${total}")
   print("-" * 30)
   print()

# --- main ---

if __name__ == "__main__":
   while True:
      print('''Menu:
         0. Agregar Snack
         1. Mostrar Snacks
         2. Comprar Snacks
         3. Mostrar Ticket
         4. Salir
         ''')
      opcion = int(input("Escoja una opcion: "))
      if opcion == 1:
         mostrar_snacks()
      elif opcion == 2:
         comprar_snacks()
      elif opcion == 3:
         mostrar_ticket()
      elif opcion == 4:
         print("\nSaliendo del sistema...")
         break
      elif opcion == 0:
         agregar_snack()
      else:
         print("Opcion invalida, proporcione una opcion valida")