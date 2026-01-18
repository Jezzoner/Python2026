print("="*40)
print("*"*5, "CONTADOR DE VOCALES", "*"*5)
print("="*40)

# Declarar la variable
cadena = "Hola Mundo"
vocales = 0
# Agregar el ciclo for 
for letra in cadena:
   if letra.lower() in "aeiou":
      vocales += 1

# Imprimir la cantidad de vocales encontradas en la cadena
print(vocales)