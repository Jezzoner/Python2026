print("="*40)
print("*"*5, "PROMEDIO DE CALIFICACIONES", "*"*5)
print("="*40)

calificaciones = []
num_calificaciones = int(input("Ingrese el No. de Calificaciones a evaluar: "))

if num_calificaciones >= 1:
   for i in range(num_calificaciones):
      nota = float(input(f"Calificacion [{i+1}] = "))
      calificaciones.append(nota)
else:
   print("Valor invalido")

print(f"\nLas calificaciones proporcionadas son: {calificaciones}")

suma = sum(calificaciones)
promedio = suma / num_calificaciones

print(f"\nEl promedio de las {num_calificaciones} calificaciones es: {promedio:.2f}")