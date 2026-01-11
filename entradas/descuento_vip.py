print("*"*5, "SISTEMA DESCUENTOS VIP", "*"*5)

NO_PRODUCTOS_DESCUENTO = 10
cant_produtos = int(input("Cuantos produtos compraste hoy: "))
tiene_membresia = input("Tienes la membresia de la tienda(si/no)?: ")

es_elegible_descuento = (cant_produtos >= NO_PRODUCTOS_DESCUENTO
                         and tiene_membresia.strip().lower() == "si")

print(f"Tienes acceso al descuento VIP?: {es_elegible_descuento}")

print("-"*30)