print("="*40)
print("*"*5, "SISTEMA DE AUTENTICACION", "*"*5)
print("="*40)

#Constantes
USUARIO_VALIDO = "admin"
PASSWORD_VALIDO = 1234

#Inputs
usuario = input("Ingrese su usuario: ")
password = int(input("Ingrese su password: "))

#Logica
if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
   print("Ingreso Exitoso, Bienvenido al sistema")
elif usuario != USUARIO_VALIDO and password == PASSWORD_VALIDO:
   print("Usuario invalido")
elif password != PASSWORD_VALIDO and usuario == USUARIO_VALIDO:
   print("Password invalido")
else:
   print("Usuario y Password invalidos")