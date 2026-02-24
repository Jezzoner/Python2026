print("="*40)
print("*"*5, "Leer archivo con Python", "*"*5)
print("="*40)

nombre_archivo = 'mi_archivo.txt'

#leer un archivo usando el metodo readlineas
with open(nombre_archivo, 'r') as archivo:
   #leer todas las lineas del archivo
   #print(archivo.readlines())
   lineas = archivo.readlines()
   for linea in lineas:
      print(linea)

print()
#leer el contenido del archivo usando read
with open(nombre_archivo, 'r') as archivo:
   print(archivo.read())