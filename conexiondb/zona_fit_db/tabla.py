import tkinter as tk
from tkinter import ttk
from cliente_dao import ClienteDAO
# No necesitas importar Cliente ni Conexion aquí si solo vas a leer datos

# --- CONFIGURACIÓN DE VENTANA ---
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.configure(background='#1d2d44')
ventana.title('Manejo de Tabla')

ventana.columnconfigure(0, weight=1)

# --- ESTILOS ---
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('Treeview', background='black',
                  foreground='white',
                  fieldbackground='black',
                  rowheight=30)
estilos.map('Treeview', background=[('selected', '#3a86ff')])

# --- DEFINICIÓN DE COLUMNAS ---
columnas = ('id', 'nombre', 'apellido', 'membresia')
tabla = ttk.Treeview(ventana, columns=columnas, show='headings')

tabla.heading('id', text='id', anchor=tk.CENTER)
tabla.heading('nombre', text='Nombre', anchor=tk.W)
tabla.heading('apellido', text='Apellido', anchor=tk.W)
tabla.heading('membresia', text='Membresia', anchor=tk.W)

tabla.column('id', width=40)
tabla.column('nombre', width=120)
tabla.column('apellido', width=120)
tabla.column('membresia', width=120)

# --- CARGAR DATOS DESDE LA BASE DE DATOS ---

# 1. Llamamos al método seleccionar de tu DAO
clientes_db = ClienteDAO.seleccionar()

# 2. Convertimos la lista de objetos en una tupla de tuplas
# IMPORTANTE: Asegúrate de que los nombres de los atributos (.id, .nombre, .edad) 
# coincidan con los que definiste en tu clase Cliente.
datos = tuple((c.id, c.nombre, c.apellido, c.membresia) for c in clientes_db)

# 3. Insertar los datos en la tabla de Tkinter
for persona in datos:
   tabla.insert(parent='', index=tk.END, values=persona)

# Agregamos un scrollbar
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

# --- PUBLICAR Y EJECUTAR ---
tabla.grid(row=0, column=0, sticky=tk.NSEW)
ventana.mainloop()