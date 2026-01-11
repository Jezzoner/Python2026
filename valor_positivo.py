print("="*40)
print("*"*5, "REVISION VALOR POSITIVO", "*"*5)
print("="*40)

numero = int(input("Ingrese un numero: "))

if numero > 0:
    print(f"Es positivo: {numero}")
elif numero < 0:
    print(f"Es negativo: {numero}")
else:
    print(f"Es cero: {numero}")