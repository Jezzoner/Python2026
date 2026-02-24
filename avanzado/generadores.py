print('*** Generadores en Python ***')

def generador(maximo):
   contador = 0
   while contador < maximo:
      yield contador
      contador += 1

# Cramos un generador
var_generador = generador(10)

# Iteramos sobre el generador
for valor in var_generador:
   print(valor)

print('*** Expresiones Generadores ***')

generador = (x**2 for x in range(10) if x % 2 == 0)

for cuadrado_pares in generador:
   print(cuadrado_pares)