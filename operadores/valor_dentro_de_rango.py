from operator import and_

print("="*40)
print("*"*5, "SISTEMA DE VALOR DENTRO DE RANGO", "*"*5)
print("="*40)

MINIMO = 0
MAXIMO = 5

dato = int(input(f"Proporcione un dato entre {MINIMO} y {MAXIMO}: "))

valor_dentro_de_rango = dato >= MINIMO and dato <= MAXIMO

print(f"Valor dentro de rango: {valor_dentro_de_rango}")

print("="*40)