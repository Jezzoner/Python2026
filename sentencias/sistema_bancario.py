print("="*40)
print("*"*5, "SISTEMA BANCARIO", "*"*5)
print("="*40)

pregunta_txt = input("Desea salir del sistema(si/no)?: ")
pregunta = pregunta_txt.lower().strip() == "si"

if not pregunta:
    print("Continuamos dentro del sistema...")
else:
    print("Saliendo del sistema...")