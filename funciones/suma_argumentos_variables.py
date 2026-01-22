print("="*40)
print("*"*5, "Suma con Argumentos Variables", "*"*5)
print("="*40)

def sumar(*args):
   total = 0
   for numero in args:
      total += numero
   return total

resultado = sumar(1,2,3,4,5)
print(f"Resultado de la suma: {resultado}")