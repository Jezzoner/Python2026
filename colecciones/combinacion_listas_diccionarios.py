print("="*40)
print("*"*5, "LISTAS CON DICCIONARIOS", "*"*5)
print("="*40)


personas = [
   {
      'nombre':'Regina',
      'apellido':'Flores',
      'edad':21
   },
   {
      'nombre':'Alejandro',
      'apellido':'Reyes',
      'edad':32
   }
]

print(personas)

#mostrar info individualmente
print(f'''
   Nombre: {personas[1]['nombre']}
   Apellido: {personas[1]['apellido']}
   Edad: {personas[1]['edad']}
      ''')

#Iterar sobre toda la lista y diccionario

for contador, persona in enumerate(personas):
   print(f''' 
{contador}  Nombre: {personas[contador]['nombre']}
   Apellido: {personas[contador]['apellido']}
   Edad: {personas[contador]['edad']}''')