print("="*40)
print("*"*5, "App Salud y Fitness", "*"*5)
print("="*40)

#Constantes
META_PASOS_DIARIO = 1000
CALORIA_POR_PASO = 0.04

#Inputs
nombre_usuario = input("Ingrese su nombre del usuario: ")
pasos_diario = int(input("Ingrese los pasos caminados en el dia: "))

#Calculo
calorias_quemadas = pasos_diario * CALORIA_POR_PASO
meta_alcanzada = pasos_diario >= META_PASOS_DIARIO

print("="*40)
print("***RESULTADOS***")
print("Hola, ", nombre_usuario)
print("Meta alcanzada" if meta_alcanzada else "Meta no alcanzada")
print("Pasos del dia de hoy: ", pasos_diario)
print(f"Tus calorias quemadas son: {calorias_quemadas:.2f} kcal")
print("="*40)