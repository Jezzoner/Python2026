import os.path
from snack import Snack

class ServicioSnacks:

   NOMBRE_ARCHIVO = 'snacks.txt'

   def __init__(self):
      self.snacks = []
      if os.path.isfile(self.NOMBRE_ARCHIVO):
         self.snacks = self.obtener_snacks()
      else:
         self.cargar_snacks_iniciales()

   def cargar_snacks_iniciales(self):
      snack_iniciales = [
         Snack('Papas', 70),
         Snack('Refresco', 50),
         Snack('Sandwich', 120),
      ]
      self.snacks.extend(snack_iniciales)
      self.guardar_snacks_archivo(snack_iniciales)

   def guardar_snacks_archivo(self, snacks):
      try:
         with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
            for snack in snacks:
               archivo.write(f"{snack.escribir_snack()}\n")
      except Exception as e:
         print(f"Error al guardar el archivo: {e}")

   def obtener_snacks(self):
      snacks = []
      try:
         with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
            for linea in archivo:
               id_snack, nombre, precio = linea.strip().split(',')
               snack = Snack(nombre, float(precio))
               snacks.append(snack)
      except Exception as e:
         print(f"Error al leer archivo de snacks: {e}")
      return snacks


      print(f"\nSnacks disponibles:\n")
      for snack in self.snacks:
         self.obtener_snacks(snack)

   def agregar_snack(self, snack):
      self.snacks.append(snack)
      self.guardar_snacks_archivo([snack])

   def mostrar_snacks(self, snack):
      print(f"--- Snacks en el Inventario ---")
      for snack in self.snacks:
         print(snack)

   def get_snacks(self):
      return self.snacks

   @property
   def snacks(self):
      return self.snacks