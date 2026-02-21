class Libro:

   count = 0

   def __init__(self, titulo=str, autor=str, genero=str):
      self._titulo = titulo
      self._autor = autor
      self._genero = genero
      Libro.count += 1
      self.id = Libro.count

   #Encapsulamiento de titulo
   @property
   def titulo(self):
      return self._titulo
   
   #Encapsulamiento de autor
   @property
   def autor(self):
      return self._autor
   
   #Encapsulamiento de genero
   @property
   def genero(self):
      return self._genero
   
   #Metodo de contador de libros
   @classmethod
   def total_libros(cls):
      return cls.count