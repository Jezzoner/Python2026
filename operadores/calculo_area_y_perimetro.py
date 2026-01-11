print("="*40)
print("*"*5, "CALCULO AREA Y PERIMETRO DE UN RECTANGULO", "*"*5)
print("="*40)

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

area = base * altura
perimetro = 2 * (base + altura)

print("="*40)
print("RESULTADOS DE AREA Y PERIMETRO")
print("="*40)
print(f"El area del rectangulo es:       {area:.2f}")
print(f"El perimetro del rectangulo es:  {perimetro:.2f}")
print("="*40)