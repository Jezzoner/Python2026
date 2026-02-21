class Libro:

   count = 0

   def __init__(self, titulo, autor, genero):
      self.titulo = titulo
      self.autor = autor
      self.genero = genero
      Libro.count += 1
      self.id = Libro.count

   #Encapsulamiento de titulo
   @property
   def titulo(self):
      return self.titulo
   
   @titulo.setter
   def titulo(self, titulo):
      self.titulo = titulo
   
   #Encapsulamiento de autor
   @property
   def autor(self):
      return self.autor
   
   @autor.setter
   def autor(self, autor):
      self.autor = autor
   
   #Encapsulamiento de genero
   @property
   def genero(self):
      return self.genero
   
   @genero.setter
   def genero(self, genero):
      self.genero = genero
   
   #Metodo de contador de libros
   @classmethod
   def total_libros(cls):
      return cls.count