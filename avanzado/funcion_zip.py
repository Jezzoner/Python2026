print("="*40)
print("*"*5, "Comprension de Listas", "*"*5)
print("="*40)

nombres = ['Juan', 'Maria', 'Pedro', 'Ana']
edades = [30, 25, 35]
ciudades = ['Madrid', 'Barcelona', 'Sevilla']

# Combinar los elementos correspondientes usando la funcion zip
personas = zip(nombres, edades, ciudades)

# Iterar sobre el resultado de la funcion zip
for persona in personas:
   print(persona)