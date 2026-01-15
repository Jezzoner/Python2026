print("="*40)
print("*"*5, "CREACION Y VALIDACION DE CONTRASEÑAS", "*"*5)
print("="*40)

password = input("Ingresa una contraseña(Debe tener al menos 6 caracteres): ")

while len(password) < 6:
   print("La contraseña no cumple con los requisitos. Debe tener al menos 6 caracteres.\n")
   password = input("Ingresa una contraseña valida: \n")
else:
   print("Contraseña valida. Felicidades!")