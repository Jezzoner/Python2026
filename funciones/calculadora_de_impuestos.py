print("="*40)
print("*"*5, "Calculadora de Impuestos", "*"*5)
print("="*40)

def mostrar_menu():
   print('''\nOperaciones que puedes realizar:    
      1. Calcular impuestos
      2. Otra opción (Futura)
      3. Salir
      ''')
   return int(input("Escoge una opcion: "))

def pedir_valores():
   pago = float(input("\nIngrese el pago sin impuestos: "))
   porcentaje = float(input("Ingrese el el monto del impuesto: "))
   return pago, porcentaje

def calculo_impuesto(pago, porcentaje):
   return pago + (pago * (porcentaje/100))

if __name__ == "__main__":
   while True:
      opcion = mostrar_menu()

      if opcion == 3:
         print("\nGracias por usar la calculadora de impuestos")
         break
      if 1 <= opcion <= 2:
         if opcion == 1:
            # 1. Pedimos datos
            pago , porcentaje = pedir_valores()
            # 2. Calculamos UNA VEZ y guardamos en variable
            total = calculo_impuesto(pago, porcentaje)
            # 3. Mostramos la variable
            print(f"\nEl pago total con impuestos es: ${total:.2f}")
         elif opcion == 2:
            print("Opcion aun no añadida (En construccion...)")
      else:
         print("Opcion invalida, proporcione una opcion valida")