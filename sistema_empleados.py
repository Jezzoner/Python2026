print("*"*5, "SISTEMA DE EMPLEADOS", "*"*5)

nombre_empleado = input("Ingrese nombre de empleado: ")
edad_empleado = int(input("Ingrese edad de empleado: "))
salario_empleado = float(input("Ingrese salario de empleado: "))
jefe_departamento = input("Ingrese jefe_departamento(si/no): ")

jefe_departamento = jefe_departamento.strip().lower() == "si"

print("="*50)
print("*"*5, "SISTEMA DE EMPLEADOS", "*"*5)
print("="*50)
print("\nDatos del Empleado")
print(f"Nombre: {nombre_empleado}")
print(f"Edad: {edad_empleado}")
print(f"Salario: {salario_empleado}")
print(f"Jefe de Departamento: {jefe_departamento}\n")
print("="*50)
