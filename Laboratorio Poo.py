import tkinter as tk

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.__edad=edad
    
    def mostrar_info(self):
        return f"nombre:{self.nombre}, Edad: {self.__edad}"
    
    def presentarse(self):
        return f"hola, soy {self.nombre}."
        

class Estudiante(Persona):
    def __init__(self,nombre,edad,carrera):
        super().__init__(nombre,edad)
        self.carrera=carrera

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self._Persona__edad}, Carrera: {self.carrera}"

    def presentarse(self):
        return f"Hola, soy {self.nombre} y estudio {self.carrera}."

# ===============================
# Funciones de la interfaz gráfica
# ===============================

def crear_persona():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    persona = Persona(nombre, edad)
    label_resultado.config(
        text=persona.mostrar_info() + "\n" + persona.presentarse()
    )

def crear_estudiante():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    carrera = entry_carrera.get()
    estudiante = Estudiante(nombre, edad, carrera)
    label_resultado.config(
        text=estudiante.mostrar_info() + "\n" + estudiante.presentarse()
    )

def limpiar_pantalla():
    label_resultado.config(text="")

# ===============================
# Interfaz con Tkinter
# ===============================
root = tk.Tk()
root.title("Laboratorio POO")

tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Edad:").pack()
entry_edad = tk.Entry(root)
entry_edad.pack()

tk.Label(root, text="Carrera:").pack()
entry_carrera = tk.Entry(root)
entry_carrera.pack()

tk.Button(root, text="Crear Persona", command=crear_persona).pack(pady=5)
tk.Button(root, text="Crear Estudiante",
          command=crear_estudiante).pack(pady=5)
tk.Button(root, text="Limpiar", command=limpiar_pantalla).pack(pady=5)

label_resultado = tk.Label(root, text="", fg="purple")
label_resultado.pack()

root.mainloop()
