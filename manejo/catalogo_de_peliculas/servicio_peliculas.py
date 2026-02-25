import os.path
from pelicula import Pelicula

class ServicioPeliculas:

   FILENAME = 'peliculas.txt'

   def __init__(self):
      self.movies = []
      if os.path.isfile(self.FILENAME):
         self.movies = self.obtener_peliculas()
      else:
         print("Sin catalogo...")
   
   def guardar_peliculas_en_archivo(self, movies):
      try:
         with open(self.FILENAME, 'a') as file:
            for movie in movies:
               file.write(f"{movie.escribir_pelicula()}\n")
      except Exception as e:
         print(f"Error al guardar el archivo: {e}")

   def obtener_peliculas(self):
      movies = []
      try:
         with open(self.FILENAME, 'r') as file:
            for line in file:
               id_movie, name, duration, gender = line.strip().split(',')
               movie = Pelicula(name,int(duration),gender)
               movies.append(movie)
      except Exception as e:
         print(f"Error al leer archivo de peliculas: {e}")
      return movies

   def agregar_pelicula(self, movie):
      self.movies.append(movie)
      self.guardar_peliculas_en_archivo([movie])

   def listar_peliculas(self):
      if not self.movies:
         print("\n* No existe catalogo de peliculas *")
      else:
         print("\n--- Peliculas disponibles ---\n")
         for movie in self.movies:
            print(movie)

   def eliminar_catalogo(self):
      try:
         if os.path.exists(self.FILENAME):
            os.remove(self.FILENAME)
            self.movies.clear()
            print(f"\nCatalogo {self.FILENAME} eliminado exitosamente")
         else:
            print("\nNo hay catalogo que eliminar")
      except Exception as e:
         print(f"\nError al guardar el archivo: {e}")

#   def get_movies(self):
#      return self.movies