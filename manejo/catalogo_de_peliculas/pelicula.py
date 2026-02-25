class Pelicula:
   
   count = 0

   def __init__(self,name=str, duration =int, gender=str):
      Pelicula.count += 1
      self.id_movie = Pelicula.count
      self.name = name
      self.duration = duration
      self.gender = gender
   
   def __str__(self):
      return (f"Pelicula -> ID: {self.id_movie}, Nombre: {self.name}, Duracion: {self.duration}min, Genero: {self.gender}")
   
   def escribir_pelicula(self):
      return f"{self.id_movie}, {self.name}, {self.duration}, {self.gender}"
   