print("="*40)
print("*"*5, "Reserva de Hotel", "*"*5)
print("="*40)
#Constantes
HAB_VISTA_AL_MAR = 190.50
HAB_SIN_VISTA_AL_MAR = 150.50
#Inputs
nombre_cliente = input("Ingrese nombre del cliente: ")
dias_de_estadia = int(input("Ingrese los dias de estadia: "))
hab_con_vista = input("Habitacion vista al mar(si-no)?: ")
hab_con_vista = hab_con_vista.strip().lower() == "si"

#if hab_con_vista:
#    costo_total = HAB_VISTA_AL_MAR * dias_de_estadia
#else:
#    costo_total = HAB_SIN_VISTA_AL_MAR * dias_de_estadia

#Operador ternario
costo_total = HAB_VISTA_AL_MAR * dias_de_estadia if hab_con_vista else HAB_SIN_VISTA_AL_MAR * dias_de_estadia

print("="*40)
print("***Detalles de la Reservacion del Hotel***")
print(f"Cliente: {nombre_cliente}")
print(f"Dias de estadia: {dias_de_estadia}")
print(f"Costo total: ${costo_total:.2f}")
print(f"Habitacion con vista al mar: ", "SI" if hab_con_vista else "NO")
print("="*40)