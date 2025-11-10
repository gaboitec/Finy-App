import tkinter as tk
#from tkinter import ttk

class HomeView(tk.Frame):
    def __init__(self, master, usuario, servicios):
        super().__init__(master)
        self.usuario = usuario
        self.servicios = servicios
        self.configure(bg="white")
        self.pack(fill="both", expand=True)
        self._construir_interfaz()

    def _construir_interfaz(self):
        # Frame principal dividido en menú y contenido
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Menú lateral
        menu_frame = tk.Frame(self, bg="#FF8000", width=180)
        menu_frame.grid(row=0, column=0, sticky="ns")
        menu_frame.grid_propagate(False)

        nombre_usuario = f"Hola, {self.usuario.nombre}"
        lbl_usuario = tk.Label(menu_frame, text=nombre_usuario, bg="#FF8000", fg="white", font=("Helvetica", 14, "bold"))
        lbl_usuario.pack(pady=(80, 80))

        opciones = ["Inicio", "Transacciones", "Presupuestos", "Deudas", "Deudores"]
        for texto in opciones:
            btn = tk.Button(menu_frame, text=texto, bg="#FF8000", fg="white", font=("Helvetica", 12), bd=0, anchor="w")
            btn.pack(fill="x", padx=40, pady=5)

    def _cambiar_vista(self, vista_clase):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        nueva_vista = vista_clase(self.content_frame, self.usuario, self.servicios)
        nueva_vista.pack(fill="both", expand=True)