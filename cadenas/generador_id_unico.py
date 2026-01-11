from random import randint

#numero_aleatorio = randint(1,6)
#print(f"El numero aleatorio es {numero_aleatorio}")

print("*"*5, "SISTEMA GENERADOR DE ID UNICO", "*"*5)

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
ano_nacimiento = input("Ingrese su año de nacimiento(YYYY): ")
valor_aleatorio = randint(1000, 9999)

nombre_normalizado = nombre.strip().upper()[0:2]
apellido_normalizado = apellido.strip().upper()[0:2]
ano_nacimiento_normalizado = ano_nacimiento.strip()[2:4]

print("="*50)
print(f"Tu ID unico es: {nombre_normalizado}{apellido_normalizado}{ano_nacimiento_normalizado}{valor_aleatorio}")
print("="*50)