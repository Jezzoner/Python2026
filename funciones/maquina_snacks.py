print("="*40)
print("*"*5, "Maquina de Snacks", "*"*5)
print("="*40,"\n")

snacks = [
   {'id': 1, 'nombre': 'Papas', 'precio': 30},
   {'id': 2, 'nombre': 'Refresco', 'precio': 50},
   {'id': 3, 'nombre': 'Sandwich', 'precio': 120}
]
compras = []
id = 1

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

#Opcion 2
def comprar_snacks(snack_a_comprar):
   for snack in snacks:
      if snack.get('id') == snack_a_comprar:
            print(f'\nSnack agregado --> ID: {snack.get('id')}, Nombre: {snack.get('nombre')}, Precio: ${snack.get('precio')}\n')
            global id
            snack = {
               'id': id,
               'nombre': snack.get('nombre'),
               'precio': snack.get('precio')
            }
            compras.append(snack)
            id += 1
            return
   print(f"\nSnack NO encontrado con ID: {snack_a_comprar}\n")

#Opcion 3
def mostrar_ticket():
   print()
   print("-"*4, "Ticket de Venta", "-"*4,"\n")
   total = 0
   for compra in compras:
      print(f"- {compra.get('nombre')} ... ${compra.get('precio')}")
      total = total + compra.get('precio')
   print(f"\nTOTAL --> ${total}\n")


if __name__ == "__main__":
   while True:
      print('''Menu:
         1. Mostrar Snacks
         2. Comprar Snacks
         3. Mostrar Ticket
         4. Salir
         ''')
      opcion = int(input("Escoja una opcion: "))
      if opcion == 1:
         mostrar_snacks()
      elif opcion == 2:
         snack_a_comprar = int(input("\nQue Snack quieres comprar (ID): "))
         comprar_snacks(snack_a_comprar)
      elif opcion == 3:
         print(compras)
         mostrar_ticket()
      elif opcion == 4:
         print("\nSaliendo del sistema...")
         break
      else:
         print("Opcion invalida, proporcione una opcion valida")