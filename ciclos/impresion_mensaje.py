print("="*40)
print("*"*5, "REPETICION DE UN MENSAJE", "*"*5)
print("="*40)


mensaje = input("Proporciona un mensaje a repetir: ")
num_repeticiones = int(input("Cuantas veces quieres que se repita?: "))

for i in range(num_repeticiones):
   print(f"{i+1} - {mensaje}")