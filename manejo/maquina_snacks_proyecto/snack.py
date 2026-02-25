class Snack:

   contador = 0

   def __init__(self, nombre='',precio=0.0):
      Snack.contador += 1
      self.id_snack = Snack.contador
      self.nombre = nombre
      self.precio = precio

   def __str__(self):
      return (f'snack id: {self.id_snack}, nombre: {self.nombre}, '
      f'precio: {self.precio}')

   def escribir_snack(self):
      return f"{self.id_snack}, {self.nombre}, {self.precio}"
   
   