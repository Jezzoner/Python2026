print("="*40)
print("*"*5, "Funciones Recursivas", "*"*5)
print("="*40)

def funcion_recursiva(numero):
   if numero == 1:
      print(numero, end=' ')
   else:
      funcion_recursiva (numero - 1)
      print(numero, end=' ')

#numero = int(input("Ingrese un numero: "))
funcion_recursiva(100)