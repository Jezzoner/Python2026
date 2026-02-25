class Snack:

   contador = 0

   def __init__(self, nombre=str,precio=float):
      Snack.contador += 1
      self.id_snack = Snack.contador
      self.nombre = nombre
      self.precio = precio

   def __str__(self):
      return (f'Snack -> ID: {self.id_snack}, Nombre: {self.nombre}, '
      f'Precio: ${self.precio:.2f}')

   def escribir_snack(self):
      return f"{self.id_snack}, {self.nombre}, {self.precio}"
   
   