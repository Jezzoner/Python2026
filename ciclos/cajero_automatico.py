print("="*40)
print("*"*5, "APLICACION DE CAJERO AUTOMATICO", "*"*5)
print("="*40)

salida = False
saldo = 1000.00

while not salida:
   print(f'''Operaciones que puedes realizar:
   1. Consultar saldo
   2. Retirar
   3. Depositar
   4. Salir''')
   opcion = int(input("Escoja una opcion: "))
   if opcion == 1:
      print(f"Tu saldo actual es: ${saldo:.2f}\n")
   elif opcion == 2:
      retiro = float(input("Cuanto quieres retirar?: "))
      if retiro < saldo:
         saldo = saldo - retiro
         print(f"Tu nuevo saldo es: ${saldo:.2f}\n")
      else:
         print(f"No cuentas con el saldo suficiente. Tu saldo actual es: {saldo:.2f}\n")
      #saldo = saldo - retiro if saldo > retiro else "No cuentas con el saldo suficiente. Tu saldo actual es: ", saldo
   elif opcion == 3:
      deposito = float(input("Cuanto quieres depositar?: "))
      saldo = saldo + deposito
      print(f"Tu nuevo saldo es: ${saldo:.2f}\n")
   elif opcion == 4:
      print("Saliendo del sistema...\n")
      salida = True
   else:
      print("Opcion invalida\n")
else:
   print("Gracias por usar nuestro cajero automatico")
