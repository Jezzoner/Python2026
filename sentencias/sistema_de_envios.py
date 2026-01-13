print("="*40)
print("*"*5, "SISTEMA DE ENVÍOS", "*"*5)
print("="*40)

#Constantes de costos de envío
NACIONAL = 10
INTERNACIONAL = 20

#Inputs
destino = int(input("Destino\n(1)Nacional \n(2)Internacional\nSeleccione destino: "))
destino = destino == 1
peso = float(input("Ingrese el peso(km) del paquete: "))

#Logica
costo_envio = peso * NACIONAL if destino else peso * INTERNACIONAL
#Impresion
print("="*40)
print("Destino: ", "Nacional" if destino else "Internacional")
print("Peso:  ", peso,"kg")
print("El costo de envio es: $", costo_envio)
print("="*40)