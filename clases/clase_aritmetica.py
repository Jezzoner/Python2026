print("="*40)
print("*"*5, "Clase Aritmetica", "*"*5)
print("="*40)

class Aritmetica:

   #Constructor
   def __init__(self, operando1=None, operando2=None):
      self._operando1 = operando1
      self._operando2 = operando2

   def suma(self):
      resultado = self._operando1 + self._operando2
      print(F"El resultado de la suma es: {resultado}")

   def resta(self):
      resultado = self._operando1 - self._operando2
      print(F"El resultado de la resta es: {resultado}")   

   def multiplicacion(self):
      resultado = self._operando1 * self._operando2
      print(F"El resultado de la multiplicacion es: {resultado}")

   def division(self):
      resultado = self._operando1 / self._operando2
      print(F"El resultado de la division es: {resultado}")

   @property
   def operando1(self):
      return self._operando1
   
   @operando1.setter
   def operando1(self, operando1):
      self._operando1 = operando1

   @property
   def operando2(self):
      return self._operando2
   
   @operando2.setter
   def operando2(self, operando2):
      self._operando2 = operando2


if __name__ == "__main__":
   print("***Ejemplo Clase Aritmetica***")
   aritmetica1 = Aritmetica(5,4) #9
   print(f"Valor operando1 del objeto aritmetica1: {aritmetica1.operando1}")
   print(f"Valor operando2 del objeto aritmetica1: {aritmetica1.operando2}")
   aritmetica1.suma()
   aritmetica1 = Aritmetica(10,4) #6
   aritmetica1.resta()
   aritmetica1 = Aritmetica(2,4) #8
   aritmetica1.multiplicacion()
   aritmetica1 = Aritmetica(5,2) #2.5
   aritmetica1.division()
   aritmetica1.operando1 = 20
   aritmetica1.operando2 = 40
   print(f"Valor operando1 del objeto aritmetica1: {aritmetica1.operando1}")
   print(f"Valor operando2 del objeto aritmetica1: {aritmetica1.operando2}")


   print()
   aritmetica2 = Aritmetica(120,230) #9
   print(f"Valor operando1 del objeto aritmetica2: {aritmetica2.operando1}")
   print(f"Valor operando2 del objeto aritmetica2: {aritmetica2.operando2}")
   aritmetica2.suma()
   aritmetica2 = Aritmetica(300,200) #6
   aritmetica2.resta()
   aritmetica2 = Aritmetica(20,5) #8
   aritmetica2.multiplicacion()
   aritmetica2 = Aritmetica(500,2) #2.5
   aritmetica2.division()