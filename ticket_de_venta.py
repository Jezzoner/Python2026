print("="*40)
print("*"*5, "GENERACION DE TICKET DE VENTA", "*"*5)
print("="*40)

precio_leche = float(input("Ingrese el precio de la leche: "))
precio_pan = float (input("Ingrese el precio del pan: "))
precio_lechuga = float (input("Ingrese el precio de la lechuga: "))
precio_platano = float (input("Ingrese el precio del platano: "))
descuento_porcentaje = int(input("Aplicar algun descuento(%)?: "))

subtotal = precio_leche + precio_pan + precio_lechuga + precio_platano

descuento = subtotal * (descuento_porcentaje / 100)

subtotal_con_descuento = subtotal - descuento

impuesto = subtotal_con_descuento * 0.16

total = subtotal_con_descuento + impuesto

print("="*40)

print(f'''
Subtotal:                        ${subtotal:.2f}
Descuento:                       ${descuento:.2f} ({descuento_porcentaje}%)
Subtotal con descuento:          ${subtotal_con_descuento:.2f}
Impuesto (16%):                  ${impuesto:.2f}
Costo total de la compra:        ${total:.2f}
''')

print("="*40)
