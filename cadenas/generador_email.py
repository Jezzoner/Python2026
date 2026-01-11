print("*"*5, "Generar email", "*"*5)

nombre_usuario = input("Ingrese su nombre: ")
nombre_empresa = input("Ingrese su empresa: ")
extension_dominio = input("Ingrese su dominio: ")

nombre_usuario_normalizado = nombre_usuario.lower().replace(" ", ".")
nombre_empresa_normalizado = nombre_empresa.lower().strip().replace(" ", "")

email_final_generado = nombre_usuario_normalizado + "@" + nombre_empresa_normalizado + extension_dominio

print("="*50)

print(f"Nombre usuario: {nombre_usuario}")
print(f"Nombre empresa: {nombre_empresa}")
print(f"Dominio: {extension_dominio}")
print(f"Email final generado: {email_final_generado}")
print("="*50)