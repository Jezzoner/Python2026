print("="*40)
print("*"*5, "ESTACION DEL AÑO", "*"*5)
print("="*40)

calificacion = float(input("Ingrese la calificacion: "))

print("*"*5, "RESULTADOS", "*"*5)

if 9 <= calificacion <= 10:
   print(f"La calificacion {calificacion} es equivalente a: 'A'")
elif 8 <= calificacion < 9:
   print(f"La calificacion {calificacion} es equivalente a: 'B'")
elif 7 <= calificacion < 8:
   print(f"La calificacion {calificacion} es equivalente a: 'C'")
elif 6 <= calificacion < 7:
   print(f"La calificacion {calificacion} es equivalente a: 'D'")
elif 0 <= calificacion <6:
   print(f"La calificacion {calificacion} es equivalente a: 'E'")
else:
   print("Valor desconocido")

print("="*40)
