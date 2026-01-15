from random import randint 

print("="*40)
print("*"*5, "ADIVINA EL NUMERO", "*"*5)
print("="*40)

game_over = False
numero_aleatorio = randint(1,50)
contador = 0

while not game_over:
   numero = int(input("Ingresa un numero: "))
   if numero != numero_aleatorio:
      print("Numero incorrecto")
      contador += 1
      print("El numero es menor al introducido" if numero > numero_aleatorio else "El numero es mayor al introducido")
      print(f"Numero de intentos fallidos: {contador} / 10\n")
      if contador == 10:
         print("Game Over")
         print(f"El numero era: {numero_aleatorio}.")
         game_over = True
   else:
      print(f"FELICIDADES, el numero correcto es: {numero_aleatorio}")
      game_over = True
else:
   print("Gracias por jugar 'ADIVINA EL NUMERO'.")
