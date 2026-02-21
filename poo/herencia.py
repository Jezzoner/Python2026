class Animal:
   def comer(self):
      print("Como muchas veces al dia")
   
   def dormir(self):
      print("Duermo muchas horas")

class Perro(Animal):
   def hacer_sonido(self):
      print("Puedo ladrar")
   
   #Sobreescritura
   def dormir(self):
      print("Duermo 15 horas al dia")

class Gato(Animal):
   def hacer_sonido(self):
      print

# Programa principal
print('*** Ejemplo de Herencia en Python ***\n')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir() #metodo sobreescrito
perro1.hacer_sonido()