from dispositivos_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
   
   count_teclado = 0

   def __init__(self, marca, tipo_entrada):
      Teclado.count_teclado += 1
      self.id_teclado = Teclado.count_teclado
      super().__init__(marca, tipo_entrada)

   def __str__(self):
      return (f"ID: {self.id_teclado}, Marca: {self.marca}, "
            f"Tipo de Entrada: {self.tipo_entrada}")
   
if __name__ == "__main__":
   teclado1 = Teclado("HP", "USB")
   print(teclado1)
   teclado2 = Teclado("DELL", "Bluetooth")
   print(teclado2)