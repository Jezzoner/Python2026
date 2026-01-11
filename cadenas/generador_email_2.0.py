print("*"*5, "GENERADOR DE EMAILS 2.0", "*"*5)

nombre_usuario = input("Ingrese su nombre completo: ")
apellido_usuario = input("Ingrese su apellido completo: ")
nombre_empresa = input("Ingrese nombre de su empresa: ")
extension_dominio = input("Ingrese su dominio: ")

nombre_usuario_normalizado = nombre_usuario.strip().lower().replace(" ", ".")
apellido_usuario_normalizado = apellido_usuario.strip().lower().replace(" ", ".")
nombre_empresa_normalizado = nombre_empresa.strip().lower().replace(" ", "")
extension_dominio_normalizado = extension_dominio.strip().lower().replace(" ", "")
email_final_generado = nombre_usuario_normalizado + "." + apellido_usuario_normalizado + "@" + nombre_empresa_normalizado + extension_dominio_normalizado

print("="*50)

print(f"\nNombre usuario: {nombre_usuario}")
print(f"Apellido usuario: {apellido_usuario}")
print(f"Nombre empresa: {nombre_empresa}")
print(f"Dominio: {extension_dominio}")
print(f"Email final generado: {email_final_generado}\n")
print("="*50)