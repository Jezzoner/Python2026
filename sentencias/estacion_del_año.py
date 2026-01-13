print("="*40)
print("*"*5, "ESTACION DEL AÑO", "*"*5)
print("="*40)

mes_input = int(input("Ingrese en numeros un mes(1-12): "))

if mes_input in [12, 1, 2]:
   print("Invierno")
elif mes_input in [3, 4, 5]:
   print("Primavera")
elif mes_input in [6, 7, 8]:
   print("Verano")
elif mes_input in [9, 10, 11]:
   print("Otoño")
else:
   print("Estacion desconocida")

print("="*40)