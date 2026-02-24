from functools import reduce

print("="*40)
print("*"*5, "Funciones Lambda", "*"*5)
print("="*40)

# Funcion cuadrado sin usar lambda
def cuadrado(x):
    return x ** 2

print(f'El cuadrado de 5: {cuadrado(5)}')

# Funcion lambda (anonima)

cuadrado_lambda = lambda x: x ** 2
print(f'El cuadrado de 2: {cuadrado_lambda(2)}')
print(f'El cuadrado de 4: {cuadrado_lambda(4)}')


# Con map y lambda
# Creamos una lista de numeros
numeros = [1, 2, 3, 4, 5]

# Aplicar una funcion lambda para obtener el cuadrado de cada numero

cuadrados = list(map(lambda x: x ** 2, numeros))
print(f'Resultado de usar map y lambda: {cuadrados}')

# Con filter y lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f'Resultado de usar filter para filtrar numeros pares: {pares}')

suma_acumulativa = reduce(lambda num1, num2: num1 + num2, numeros)

print(suma_acumulativa)