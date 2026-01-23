print("="*40)
print("*"*5, "Convertidor de temperaturas(ºC/ºF)", "*"*5)
print("="*40)


def mostrar_menu():
   print('''\nOperaciones disponibles:    
      1. Convertir Celsius a Fahrenheit (ºC -> ºF)
      2. Convertir Fahrenheit a Celsius (ºF -> ºC)
      3. Salir
      ''')
   return int(input("Escoge una opcion: "))

def pedir_temperatura():
   temperatura = float(input("\nIngresa la temperatura: "))
   return temperatura

def fahrenheit_a_celsius(fahrenheit):
   return (fahrenheit - 32) / 1.8

def celsius_a_fahrenheit(celsius):
   return (celsius * 1.8) + 32

if __name__ == "__main__":
   while True:
      opcion = mostrar_menu()

      if opcion == 3:
         print("\nGracias por usar el convertidor. ¡Adiós!")
         break
      if 1 <= opcion <= 2:
         # Como ambas opciones necesitan pedir un número, lo pedimos aquí antes del IF
         temp_input = pedir_temperatura()
         
         if opcion == 1:
            resultado = celsius_a_fahrenheit(temp_input)
            print(f"\nResultado: {temp_input}ºC equivalen a {resultado:.2f}ºF")
         elif opcion == 2:
            resultado = fahrenheit_a_celsius(temp_input)
            print(f"\nResultado: {temp_input}ºF equivalen a {resultado:.2f}ºC")
      else:
         print("\n❌ Opción inválida, intenta de nuevo.")