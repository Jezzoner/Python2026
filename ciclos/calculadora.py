print("="*40)
print("*"*5, "CALCULADORA", "*"*5)
print("="*40)

salida = False

while not salida:
   print(f'''Operaciones que puedes realizar:
   1. Suma
   2. Resta
   3. Multiplicacion
   4. Division
   5. Salir''')
   opcion = int(input("Escoja una opcion: "))
   if 1 <= opcion <= 4:
      valor1 = float(input("Introduzca el primer valor: "))
      valor2 = float(input("Introduzca el segundo valor: "))
   if opcion == 1:
      resultado = valor1 + valor2
      print(f"La suma de {valor1} + {valor2} es: {resultado:.2f}\n")
   elif opcion == 2:
      resultado = valor1 - valor2
      print(f"La resta de {valor1} - {valor2} es: {resultado:.2f}\n")
   elif opcion == 3:
      resultado = valor1 * valor2
      print(f"La multiplicacion de {valor1} * {valor2} es: {resultado:.2f}\n")
   elif opcion == 4:
      resultado = valor1 / valor2
      print(f"La division de {valor1} / {valor2} es: {resultado:.2f}\n")
   elif opcion == 5:
      print("Saliendo del sistema...\n")
      salida = True
   else:
      print("Opcion invalida\n")
else:
   print("Gracias por usar la calculadora")
