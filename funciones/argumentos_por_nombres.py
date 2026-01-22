from titulos import membrete

membrete("Funcion con argumentos por nombre")

def imprimir_persona(nombre, apellido='', edad=0):
   print(f"Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}")

imprimir_persona('Ricardo', 'Quintana', 32)

imprimir_persona(nombre='Carlos',apellido='Rojas',edad=28)

imprimir_persona(apellido='Rojas',nombre='Carlos',edad=28)

imprimir_persona(nombre='Carlos')

imprimir_persona(nombre='Carlos',apellido='Rojas')