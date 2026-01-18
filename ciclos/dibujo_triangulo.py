print("="*40)
print("*"*5, "DIBUJO DE UN TRIANGULO", "*"*5)
print("="*40)

num_filas = int(input("Ingrese el numero de filas: "))

for fila in range(1, num_filas + 1):
   espacios = " " * (num_filas - fila)
   asteriscos = "*" * (2 * fila - 1)
   print(espacios, asteriscos)