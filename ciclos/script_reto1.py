print("="*40)
print("*"*5, "SCRIPT DE MANTENIMIENTO - RETO 1 GEMINI", "*"*5)
print("="*40)

servidores = ["192.168.1.10", "192.168.1.11", "192.168.1.20", "192.168.1.50"]

for servidor in servidores:
   intentos = 0
   print("-", servidor, end=' ====>\n')
   if servidor == "192.168.1.20":
      conexion_exitosa = False
      print("¡Error de conexión!")
      while intentos < 3:
         if conexion_exitosa:
            print("¡Reconexión exitosa!")
            break
         intentos += 1
         print(f"Reintentando conexión... (intento {intentos})")
      else:
         print("Abortando. Servidor caído.")
   else:
      conexion = True
      print(f" Ping exitoso: {servidor} ONLINE")