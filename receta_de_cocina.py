print("*"*5, "SISTEMA DE RECETAS DE COCINA", "*"*5)

nombre_receta = input("Ingrese el nombre de la receta: ")
ingredientes_receta = input("Ingrese los ingredientes de la receta: ")
tiempo_de_preparacion = int(input("Ingrese la tiempo de preparacion(min): "))
dificultad = input("Ingrese la dificultad(Facil, Media o Alta): ")

print("="*50)
print(f"\nNombre de la receta: {nombre_receta.upper()}")
print(f"Ingredientes de la receta: {ingredientes_receta.upper()}")
print(f"Tiempo de preparacion: {tiempo_de_preparacion}min")
print(f"Dificultad: {dificultad.upper()}\n")

print("="*50)