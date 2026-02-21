from dispositivos_entrada import DispositivoEntrada

class Monitor(DispositivoEntrada):

   count_monitor = 0

   def __init__(self, marca, tamaño):
      Monitor.count_monitor += 1
      self.id_monitor = Monitor.count_monitor
      super().__init__(marca, tipo_entrada=None)
      self.tamaño = tamaño
   
   def __str__(self):
      return (f"ID: {self.id_monitor}, Marca: {self.marca}, "
            f"Tamaño: {self.tamaño}")
   
if __name__ == "__main__":
   monitor1 = Monitor("HP", "32 Pulgadas")
   print(monitor1)
   monitor2 = Monitor("DELL", "27 Pulgadas")
   print(monitor2)