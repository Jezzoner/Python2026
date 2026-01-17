from random import randint 

print("="*40)
print("*"*5, "ADIVINA EL NUMERO", "*"*5)
print("="*40)

game_over = False
numero_aleatorio = randint(1,50)
intentos = 0
MAX_INTENTOS = 10

while not game_over:
   numero = int(input("Ingresa un numero: "))
   if numero != numero_aleatorio:
      print("Numero incorrecto")
      intentos += 1
      print("El numero es menor al introducido" if numero > numero_aleatorio else "El numero es mayor al introducido")
      print(f"Numero de intentos fallidos: {intentos} / {MAX_INTENTOS}\n")
      if intentos == 10:
         print("Game Over")
         print(f"El numero era: {numero_aleatorio}.")
         game_over = True
   else:
      print(f"FELICIDADES, el numero correcto es: {numero_aleatorio}")
      break
else:
   print("Gracias por jugar 'ADIVINA EL NUMERO'.")


#Codigo prof Udemy
'''
from random import randint

print('*** Juego de Adivinanzas ***')

numero_secreto = randint(1, 50)
intentos = 0
adivinanza = None
INTENTOS_MAXIMOS = 5

while adivinanza != numero_secreto and intentos < INTENTOS_MAXIMOS:
    adivinanza = int(input('Adivina el número secreto (1-50): '))
    # Agregamos una ayuda para orientar al jugador
    if adivinanza < numero_secreto:
        print('El número secreto es mayor')
    elif adivinanza > numero_secreto:
        print('El número secreto es menor')
    # Incrementamos la variable de intentos
    intentos += 1
# Conclusion del juego
if adivinanza == numero_secreto:
    print(f'Felicidades, adivinaste el número secreto en {intentos} intentos')
else:
    print(f'Lo siento, has agotado tus intentos máximos: {INTENTOS_MAXIMOS}')
    print(f'El número secreto era: {numero_secreto}')
'''