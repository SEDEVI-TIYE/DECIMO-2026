import tkinter as tk
from tkinter import messagebox, filedialog
import os

def guardar_datos():
    nom = entry_nombre.get().strip()
    ape = entry_apellido.get().strip()
    edad = entry_edad.get().strip()
    sexo = entry_sexo.get().strip().lower()
    asig = entry_asig.get().strip()
    carr = entry_carrera.get().strip()

    if not (nom and ape and edad and sexo and asig and carr):
        messagebox.showwarning("Atención", "Por favor, llene todos los campos.")
        return

    nombre_archivo = f"{nom}_{ape}.txt"

    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"Nombre: {nom}\nApellido: {ape}\nEdad: {edad}\n")
            archivo.write(f"Sexo: {sexo}\nAsignatura: {asig}\nCarrera: {carr}")
        messagebox.showinfo("Éxito", f"Datos guardados en {nombre_archivo}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar: {e}")

def seleccionar_y_leer():
    # Abre el explorador de archivos para seleccionar un .txt
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar registro de estudiante",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    
    if ruta_archivo:
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                # Actualizamos el Label o mostramos en ventana
                label_contenido.config(text=contenido, fg="blue")
                messagebox.showinfo("Lectura Exitosa", f"Leyendo: {os.path.basename(ruta_archivo)}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")

# Configuración de la ventana
root = tk.Tk()
root.title("Gestor de Registros Académicos")
root.geometry("450x600")

# --- SECCIÓN DE REGISTRO ---
tk.Label(root, text="REGISTRO DE DATOS", font=("Arial", 12, "bold")).pack(pady=10)

# Diccionario para crear campos más rápido
campos = ["Nombre", "Apellido", "Edad", "Sexo (h/m)", "Asignatura Favorita", "Carrera"]
entries = []

for campo in campos:
    tk.Label(root, text=f"{campo}:").pack()
    ent = tk.Entry(root)
    ent.pack()
    entries.append(ent)

# Asignamos las variables del loop para que el código anterior funcione
entry_nombre, entry_apellido, entry_edad, entry_sexo, entry_asig, entry_carrera = entries

tk.Button(root, text="Guardar Datos 💾", command=guardar_datos, bg="lightgreen").pack(pady=10)

# --- SECCIÓN DE LECTURA ---
tk.Label(root, text="------------------------------------------").pack()
tk.Label(root, text="VISUALIZADOR DE ARCHIVOS", font=("Arial", 12, "bold")).pack(pady=5)

tk.Button(root, text="Buscar y Leer Archivo 🔍", command=seleccionar_y_leer, bg="lightblue").pack(pady=5)

# Label con relieve para simular una sección de visualización
label_contenido = tk.Label(root, text="No hay datos seleccionados", justify="left", 
                           bg="white", relief="sunken", width=40, height=8, anchor="nw", padx=5, pady=5)
label_contenido.pack(pady=10)

root.mainloop()