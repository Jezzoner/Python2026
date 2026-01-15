print("="*5, "SISTEMA DE ADMINISTRACION DE CUENTAS", "="*5)

salir = False
while not salir:
   print(f'''Menu:
         1. Crear cuenta
         2. Eliminar cuenta
         3. Salir...''')
   opcion = int(input("Escoja una opcion: "))
   if opcion == 1:
      print("Creando cuenta...\n")
   elif opcion == 2:
      print("Eliminando cuenta...\n")
   elif opcion == 3:
      print("Saliendo del sistema..\n.")
      salir = True
   else:
      print("Opcion invalida\n")
else:
   print("Terminando el sistema de administracion de cuentas...")