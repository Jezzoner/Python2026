print("="*40)
print("*"*5, "Alcance de Variables", "*"*5)
print("="*40)

contador_global = 0

def incrementar_contador():
   contador_local = 0
   
   global contador_global
   contador_global += 1

   contador_local += 1

   print(f"Contador local: {contador_local}")
   print(f"Contador global: {contador_global}\n")

incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()

#contador global incrementa, mientras que la local se resetea cada que se manda a llamar la funcion
print(contador_global) #se guarda el ultimo valor
