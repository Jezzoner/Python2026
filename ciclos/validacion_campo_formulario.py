print("="*40)
print("*"*5, "VALIDACION CAMPO DE UN FORMULARIO", "*"*5)
print("="*40)

nombre_usuario = None

while not nombre_usuario:
   nombre_usuario = input("Ingresa tu nombre de usuario: ")

print(f"Nombre de usuario valido: {nombre_usuario}")