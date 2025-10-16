# app/gui/views/home_view.py

import tkinter as tk
from tkinter import ttk

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

        lbl_usuario = tk.Label(menu_frame, text="Usuario", bg="#FF8000", fg="white", font=("Helvetica", 14, "bold"))
        lbl_usuario.pack(pady=(20, 10))

        opciones = ["Nueva transacción", "Exportar", "Editar datos"]
        for texto in opciones:
            btn = tk.Button(menu_frame, text=texto, bg="#FF8000", fg="white", font=("Helvetica", 12), bd=0, anchor="w")
            btn.pack(fill="x", padx=20, pady=5)

        # Área de contenido (dashboard)
        content_frame = tk.Frame(self, bg="white")
        content_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Tarjetas resumen
        resumen_frame = tk.Frame(content_frame, bg="white")
        resumen_frame.pack(fill="x", pady=10)

        self._crear_tarjeta(resumen_frame, "Ingresos", self.servicios["analytics"].total_por_tipo(self.usuario.id)["ingreso"])
        self._crear_tarjeta(resumen_frame, "Gastos", self.servicios["analytics"].total_por_tipo(self.usuario.id)["gasto"])
        self._crear_tarjeta(resumen_frame, "Deuda pendiente", self.servicios["deuda"].total_adeudado(self.usuario.id))

        # Aquí puedes agregar gráficas con matplotlib más adelante

    def _crear_tarjeta(self, parent, titulo, valor):
        frame = tk.Frame(parent, bg="#F0F0F0", bd=1, relief="solid")
        frame.pack(side="left", expand=True, fill="x", padx=5)

        lbl_titulo = tk.Label(frame, text=titulo, font=("Helvetica", 12, "bold"), bg="#F0F0F0")
        lbl_titulo.pack(pady=(10, 0))

        lbl_valor = tk.Label(frame, text=f"Q {valor:.2f}", font=("Helvetica", 14), bg="#F0F0F0", fg="#333")
        lbl_valor.pack(pady=(5, 10))