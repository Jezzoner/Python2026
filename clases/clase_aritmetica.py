print("="*40)
print("*"*5, "Clase Aritmetica", "*"*5)
print("="*40)

class Aritmetica:

   #Constructor
   def __init__(self, operando1, operando2):
      self.operando1 = operando1
      self.operando2 = operando2

   def suma(self):
      resultado = self.operando1 + self.operando2
      print(F"El resultado de la suma es: {resultado}")

   def resta(self):
      resultado = self.operando1 - self.operando2
      print(F"El resultado de la resta es: {resultado}")   

   def multiplicacion(self):
      resultado = self.operando1 * self.operando2
      print(F"El resultado de la multiplicacion es: {resultado}")

   def division(self):
      resultado = self.operando1 / self.operando2
      print(F"El resultado de la division es: {resultado}")

if __name__ == "__main__":
   print("***Ejemplo Clase Aritmetica***")
   aritmetica1 = Aritmetica(5,4) #9
   aritmetica1.suma()
   aritmetica1 = Aritmetica(10,4) #6
   aritmetica1.resta()
   aritmetica1 = Aritmetica(2,4) #8
   aritmetica1.multiplicacion()
   aritmetica1 = Aritmetica(5,2) #2.5
   aritmetica1.division()

   print()
   aritmetica2 = Aritmetica(120,230) #9
   aritmetica2.suma()
   aritmetica2 = Aritmetica(300,200) #6
   aritmetica2.resta()
   aritmetica2 = Aritmetica(20,5) #8
   aritmetica2.multiplicacion()
   aritmetica2 = Aritmetica(500,2) #2.5
   aritmetica2.division()