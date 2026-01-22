print("="*40)
print("*"*5, "Funcion Par", "*"*5)
print("="*40)

def es_par(numero):
   if numero % 2 == 0:
      #print(f"El {numero} es par")
      return True
   else:
      #print(f"El {numero} es impar")
      return False

if __name__ == '__main__':
   numero = int(input("Proporciona un numero entero: "))
   print(f"Numero par? {es_par(numero)}")