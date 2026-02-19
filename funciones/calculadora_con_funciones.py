from art import text2art

art = text2art('Calculadora')

print("="*70)
print(art)
print("="*70)

def mostrar_menu():
   print('''\nOperaciones que puedes realizar:    
      1. Suma
      2. Resta
      3. Multiplicacion
      4. Division
      5. Salir
      ''')
   return int(input("Escoge una opcion: "))

def valores():
   a = float(input("\nIngrese el primer valor: "))
   b = float(input("Ingrese el segundo valor: "))
   return (a, b)

def suma():
   a , b = valores()
   resultado = a + b
   print(f"\nEl resultado de la suma es: {resultado:.2f}")

def resta():
   a , b = valores()
   resultado = a - b
   print(f"\nEl resultado de la resta es:  {resultado:.2f}")

def multiplicacion():
   a , b = valores()
   resultado = a * b
   print(f"\nEl resultado de la multiplicacion es:  {resultado:.2f}")

def division():
   a , b = valores()
   resultado = a / b
   print(f"\nEl resultado de la division es:  {resultado:.2f}")

if __name__ == "__main__":
   while True:
      opcion = mostrar_menu()
      if opcion == 1:
         suma()
      elif opcion == 2:
         resta()
      elif opcion == 3:
         multiplicacion()
      elif opcion == 4:
         division()
      elif opcion == 5:
         print("\nGracias por usar la calculadora")
         break
      else:
         print("Opcion invalida, proporcione una opcion valida")