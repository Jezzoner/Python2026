nombre_archivo = 'mi_archivo.txt'

with open(nombre_archivo,'a') as archivo:
   #anexar info
   archivo.write('Anexando informacion ...\n')
   archivo.write('Saliendo de anexar informacion... \n')

print(f"Se ha anexado informacion al archivo {nombre_archivo}")