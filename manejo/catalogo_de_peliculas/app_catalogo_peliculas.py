from pelicula import Pelicula
from servicio_peliculas import ServicioPeliculas
from art import text2art

class CatalogoPeliculas:
   title = text2art('Pelispedia')

   def __init__(self):
      self.catalogo = ServicioPeliculas()

   def catalogo_peliculas(self):
      exit = False
      print(CatalogoPeliculas.title)
      self.catalogo.listar_peliculas()
      while not exit:
         try:
            option = self.mostrar_menu()
            exit = self.execute_option(option)
         except ValueError:
            print("\nError: Introduce un numero valido.")
         except TypeError:
            print("\nOpcion no valida. Introduce un numero del 1 al 4. ")
   
   def mostrar_menu(self):
      print(f'''\nMenu de Peliculas:
            1. Agregar pelicula
            2. Listar peliculas
            3. Eliminar catalogo
            4. Salir''')
      return int(input("Elige una opcion(1-4): "))
   
   def execute_option(self, option):
      if option == 1:
         self.agregar_pelicula()
      elif option == 2:
         self.catalogo.listar_peliculas()
      elif option == 3:
         self.catalogo.eliminar_catalogo()
      elif option == 4:
         print("Regresa pronto!")
         return True
      else:
         print(f"\nOpcion no valida. Introduce un numero del 1 al 4.")
      return False
   
   def agregar_pelicula(self):
      name = input("\nNombre de la pelicula: ")
      duration = int(input("Duracion de la pelicula: "))
      gender = input("Genero de la pelicula: ")
      new_movie = Pelicula(name,duration,gender)
      self.catalogo.agregar_pelicula(new_movie)
      print("\n*Pelicula agregada exitosamente*")

   def eliminar_catalogo(self):
      pass

if __name__ == "__main__":
   app_init = CatalogoPeliculas()
   app_init.catalogo_peliculas()