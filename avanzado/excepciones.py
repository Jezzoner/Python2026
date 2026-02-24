print("="*40)
print("*"*5, "Excepciones", "*"*5)
print("="*40)

def dividir(numerador=int, denominador=int):
   try:
      # Revisamos si el denominador es igual a 0
      if denominador == 0:
            raise Exception('El denominador es igual a 0')
      resultado = numerador / denominador
      print(f'Resultado de la división: {resultado}')
   except Exception as e:
      print(f'Ocurrio un error: {e}')
   else:
      print(f'No ocurrió ningún error')
   finally:
      print(f'Terminamos de procesar la excepcion\n')
#Ejemplo de uso
dividir(10,2)
dividir(10,0)