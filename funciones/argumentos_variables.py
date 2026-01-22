print("="*40)
print("*"*5, "Argumentos Variables", "*"*5)
print("="*40)

def superheroe_superpoderes(superheroe, nombre, *args ):
   print(f"Superheroe: {superheroe} - {nombre} - {args}")
   for superpoder in args:
      print(f"\tSuperpoder: {superpoder}")

superheroe_superpoderes("Spiderman","Peter Parker","Insticto Aracnido", "Telaraña")

superheroe_superpoderes("Ironman","Tony Stark","Armadura", "Playboy", "Millonario")

superheroe_superpoderes("Mi vecino", "Juan Perez")