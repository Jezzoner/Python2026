from art import text2art
from empresa import Empresa
from empleado import Empleado

art = text2art('Sistema')

print("="*70)
print(art)
print("="*70)

empresa1 = Empresa('Global Mentoring')
empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('Maria', 'Marketing')
empresa1.contratar_empleado('Pedro', 'Ventas')
empresa1.contratar_empleado('Ana', 'RRHH')

print(f"Total de empleados: {Empleado.obtener_total_empleados()}")
print(f"Empleados en el departamento de ventas: "
      f"{empresa1.obtener_numero_empleados_por_departamento('Ventas')}")

empresa1.obtener_total_empleados()