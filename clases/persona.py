class Persona:

   #Constructor
   def __init__(self, nombre, apellido):
      self.nombre = nombre
      self.apellido = apellido

   def inicializar_persona(self, nombre, apellido):
      self.nombre = nombre
      self.apellido = apellido
   
   def mostrar_persona(self):
      print(f'''Persona:
            Nombre: {self.nombre}
            Apellido: {self.apellido}''')

if __name__ == "__main__":
   persona1 = Persona('Layla','Acosta')
   persona1.mostrar_persona()

   persona2 = Persona('Ian', 'Sanchez')
   persona2.mostrar_persona()