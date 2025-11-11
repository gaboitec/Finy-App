import tkinter as tk
from tkinter import messagebox

class FormularioCategoria(tk.Toplevel):
    def __init__(self, master, servicio_categoria, id_user, on_guardar):
        super().__init__(master)
        self.servicio = servicio_categoria
        self.on_guardar = on_guardar
        self.id_user = id_user
        self.title("Nueva categoría")
        self.geometry("300x150")
        self.configure(bg="white")

        tk.Label(self, text="Nombre de categoría:", bg="white").pack(pady=10)
        self.entry_nombre = tk.Entry(self, width=30)
        self.entry_nombre.pack()

        btn_guardar = tk.Button(self, text="Guardar", command=self._guardar)
        btn_guardar.pack(pady=10)

    def _guardar(self):
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Campo vacío", "Ingresa un nombre.")
            return
        self.servicio.crear_categoria(self.id_user, nombre)
        self.on_guardar()
        self.destroy()