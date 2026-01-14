print("="*40)
print("*"*5, "CASA DE LOS ESPEJOS", "*"*5)
print("="*40)

edad = int(input("Cual es tu edad?: "))
miedo = input("Tienes miedo a la oscuridad(si/no)?: ")
miedo = miedo.strip().lower() == "si"

if not miedo and edad >= 10:
    print("Puedes ingresar...")
else:
    print("No puedes ingresar...")

#Comentario de la Rama1