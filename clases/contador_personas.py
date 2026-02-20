class Persona:
   #atributo clase
   contador_personas = 0

   def __init__(self, nombre, apellido):
      #incrementamos el valor del atributo
      Persona.contador_personas += 1
      self.id = Persona.contador_personas
      self.nombre = nombre
      self.apellido = apellido

   def mostrar_persona(self):
      print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

if __name__ == '__main__':
   print("*** Ejemplo contador de objetos de tipo persona ***")
   persona1 = Persona("Jesus", "Castro")
   persona1.mostrar_persona()
   persona2 = Persona("Diana", "Castro")
   persona2.mostrar_persona()
   persona3 = Persona("Dayana", "Castro")
   persona3.mostrar_persona()
   persona4 = Persona("Ana", "Sanchez")
   persona4.mostrar_persona()

   print(f"Contador objetos Persona: {Persona.contador_personas}")