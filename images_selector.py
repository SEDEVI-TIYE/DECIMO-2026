import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Diccionario con datos
equipos = {
    "Consola Analógica": {
        "año": 1960,
        "imagen": "equipo1.png"
    },
    "Sintetizador": {
        "año": 1970,
        "imagen": "equipo2.png"
    },
    "Interfaz de Audio": {
        "año": 1990,
        "imagen": "equipo3.png"
    }
}

# Ventana
ventana = tk.Tk()
ventana.title("Equipos de Audio")

# Variable del combobox
seleccion = tk.StringVar()

# Combobox
combo = ttk.Combobox(ventana, textvariable=seleccion)
combo['values'] = list(equipos.keys())
combo.pack(pady=10)

# Label para mostrar año
label_año = tk.Label(ventana, text="")
label_año.pack()

# Label para imagen
label_imagen = tk.Label(ventana)
label_imagen.pack()

# Función al seleccionar
def mostrar_info(event):
    equipo = seleccion.get()
    datos = equipos[equipo]

    # Mostrar año
    label_año.config(text=f"Año de creación: {datos['año']}")

    # Cargar imagen
    img = Image.open(datos["imagen"])
    img = img.resize((500, 500))  # opcional
    foto = ImageTk.PhotoImage(img)

    label_imagen.config(image=foto)
    label_imagen.image = foto  # importante (evita que se borre)

# Evento cuando cambia selección
combo.bind("<<ComboboxSelected>>", mostrar_info)

ventana.mainloop()