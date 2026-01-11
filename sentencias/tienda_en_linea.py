print("="*40)
print("*"*5, "TIENDA EN LINEA", "*"*5)
print("="*40)

MONTO_COMPRA_DESC = 1000

monto_compra = float(input('Cual fue el monto de tu compra? '))
es_miembro = input('Eres miembro de la tienda (Si/No)? ')

print("="*40)

descuento = 0

if monto_compra >= MONTO_COMPRA_DESC and es_miembro.strip().lower() == 'si':
    descuento = 0.1  # Descuento del 10%
elif es_miembro.strip().lower() == 'si':
    descuento = .05  # Descuento del 5%
elif monto_compra >= MONTO_COMPRA_DESC:
    descuento = .03  # Descuento del 3%
else:
    descuento = 0

if descuento != 0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(f'Felicidades, has obtenido un descuento del {descuento * 100:.0f}%')
    print(f'Monto de la compra:                     ${monto_compra:.2f}')
    print(f'Monto del descuento:                    ${monto_descuento:.2f}')
    print(f'Monto final de la compra con descuento: ${monto_final:.2f}')
else:
    print('\nNo obtuviste ningún tipo de descuento')
    print('Te invitamos a hacerte miembro de la tienda')
    print(f'Monto final de la compra: ${monto_compra:.2f}')

print("="*40)