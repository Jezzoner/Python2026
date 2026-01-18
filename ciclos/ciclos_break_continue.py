print("="*40)
print("*"*5, "Break y Continue", "*"*5)
print("="*40)

print("\nBreak\n")
#Break rompe el ciclo
for numero in range(1,10+1):
   if numero % 2 == 0:
      print(f"El {numero} es par")
      break

print("\nContinue\n")
#Continue continua el ciclo
for numero in range(1,10+1):
   if numero % 2 != 0:
      print(f"El {numero} es impar")
      continue

'''
# Ejemplo con continue
print('\nPalabra continue: ')
for numero in range(1, 10):
   if numero % 2 == 1:  # numero impar
      continue
   print(numero)  # numeros pares
'''