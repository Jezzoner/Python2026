print("="*40)
print("*"*5, "SISTEMA DE AUTENTICACION", "*"*5)
print("="*40)

USUARIO = str("admin") #tambien "admin"
PASSWORD = str("1234") #tambien "1234"

usuario_input = input("Ingrese su usuario: ")
password_input = input("Ingrese su password: ")

validacion = usuario_input.strip() == USUARIO and password_input.strip() == PASSWORD

print(f"Datos correctos = {validacion}")

print("="*40)