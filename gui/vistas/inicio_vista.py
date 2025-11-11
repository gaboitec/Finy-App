import tkinter as tk
#from tkinter import ttk
from gui.vistas.ReporteVista import DashboardView
from gui.vistas.transacciones_vista import TransaccionesView
from gui.vistas.presupuestoVista import PresupuestosView
from gui.vistas.deudas_vista import DeudasView
from gui.vistas.deudores_vista import DeudoresView

class HomeView(tk.Frame):
    def __init__(self, master, usuario):
        super().__init__(master)
        self.usuario = usuario
        self.configure(bg="white")
        self.pack(fill="both", expand=True)
        self._construir_interfaz()
        self._cambiar_vista(DashboardView)

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

        opciones = [
            ("Inicio", DashboardView),
            ("Transacciones", TransaccionesView),
            ("Presupuestos", PresupuestosView),
            ("Deudas", DeudasView),
            ("Deudores", DeudoresView)
        ]
        for texto, vista in opciones:
            btn = tk.Button(menu_frame, text=texto, bg="#FF8000", fg="white", font=("Helvetica", 12), bd=0,
                            command=lambda v=vista: self._cambiar_vista(v))
            btn.pack(fill="x", padx=20, pady=5)

        self.content_frame = tk.Frame(self, bg="white")
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    def _cambiar_vista(self, vista_clase):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        nueva_vista = vista_clase(self.content_frame, self.usuario)
        nueva_vista.pack(fill="both", expand=True)