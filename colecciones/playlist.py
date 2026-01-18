print("="*40)
print("*"*5, "PLAYLIST DE CANCIONES", "*"*5)
print("="*40)

num = 1
lista_reproduccion = []
count = int(input("Cuantas canciones desea agregar a su playlist?: "))

if count != 0:
   for i in range(count):
      agregar = input("Agregue una cancion: ")
      lista_reproduccion.append(agregar)

print(lista_reproduccion)
print("Ordenando lista de canciones por orden alfabetico")
lista_reproduccion.sort()
print(lista_reproduccion)

for cancion in lista_reproduccion:
   print(f"    {num} - {cancion}")
   num += 1