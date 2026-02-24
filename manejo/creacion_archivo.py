#crear archivo
nombre_archivo = 'mi_archivo.txt'

with open(nombre_archivo, 'w') as archivo:
   archivo.write("Hola como esta\n")
   archivo.write("Estoy agregando informacion al archivo\n")

#archivo = open(nombre_archivo, 'w')
#archivo.write("Hola como esta\n")
#archivo.write("Estoy agregando informacion al archivo")
#archivo.close()

print(f"Se creo el archivo: {nombre_archivo}")