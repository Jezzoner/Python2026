print("="*40)
print("*"*5, "Argumentos Variables en forma de diccionario", "*"*5)
print("="*40)

# *args - arguments se pasan en forma de tupla
# **kwargs - keyword arguments (key,value) se pasan en forma de un diccionario


def superheroe_superpoderes(nombre, *args, **kwargs):
   print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')
   for superpoder in args:
      print(f"\tSuperpoder: {superpoder}")





# Llamarmos la funcion
superheroe_superpoderes('Spiderman', 'Instinto Arácnido', edad=17, empresa='Marvel')

superheroe_superpoderes('Ironman', 'Armandura','Playboy', edad=45)

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino', personalidad='Buena onda!')