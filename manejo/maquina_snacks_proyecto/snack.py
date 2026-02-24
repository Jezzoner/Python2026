class Snack:

   contador = 0

   def __init__(self, nombre=str,precio=float):
      Snack.contador += 1
      self.id_snack = Snack.contador
      self._nombre = nombre
      self._precio = precio

   def __str__(self):
      return (f'snack id: {self.id_snack}, nombre: {self.nombre}, '
      f'precio: {self.precio}')

   def escribir_snack(self):
      return f"{self.id_snack}, {self.nombre}, {self.precio}"

   #Encapsulamiento de nombre
   @property
   def nombre(self):
      return self._nombre
   
   #Encapsulamiento de precio
   @property
   def precio(self):
      return self._precio
   
   #Metodo de contador
   @classmethod
   def total_snacks(cls):
      return cls.contador