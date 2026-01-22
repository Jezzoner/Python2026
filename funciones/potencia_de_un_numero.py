print("="*40)
print("*"*5, "Potencia de un numero con funciones recursivas", "*"*5)
print("="*40)

def potencia(base,exponente):
   if exponente == 0:
      return 1
   else:
      return base * potencia(base, exponente - 1)
   
print(potencia(2,3))