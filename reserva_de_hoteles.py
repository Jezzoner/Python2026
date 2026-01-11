print(" *** Sistema de Reserva de Hoteles *** ")

tarifa_diaria = 0
tarifa_diaria_con_vista_mar = 120
tarifa_diaria_sin_vista_mar = 100

nombre_cliente = input("Ingrese nombre del cliente: ")
dias_estancia = int(input("Ingrese la cantidad de dias de estancia: "))
hab_vista_al_mar = input("Ingrese haberlo del vista al mar(si/no): ")

if hab_vista_al_mar == "si":
    tarifa_diaria = tarifa_diaria_con_vista_mar*dias_estancia
elif hab_vista_al_mar == "no":
    tarifa_diaria = tarifa_diaria_sin_vista_mar*dias_estancia
else:
    print("Habitacion invalido")

print(" *** Sistema de Reserva de Hoteles *** ")
print("Cliente: ", nombre_cliente)
print("Dias de estancia: ", dias_estancia)
print("Tarifa diaria: ", tarifa_diaria/dias_estancia, "Total: ", tarifa_diaria)
print("Habitacion con vista al mar: ", hab_vista_al_mar)