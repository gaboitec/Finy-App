# python
import tkinter as tk
#from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta

from logica.analitica_logica import AnalyticsService
from gestores.transacciones_gestor import TransactionsRepo
from gestores.presupuestos_gestor import PresupuestosRepo
from logica.deuda_logica import DeudaService
from gestores.deudas_gestor import DeudasRepo

class DashboardView(tk.Frame):
    def __init__(self, master, usuario):
        super().__init__(master)
        self.usuario = usuario
        self.servicios = {
            "analytics": AnalyticsService(TransactionsRepo(), PresupuestosRepo()),
            "deuda": DeudaService(DeudasRepo())}
        self.configure(bg="white")
        self.pack(fill="both", expand=True)
        self._construir_interfaz()

    def _construir_interfaz(self):

        # Área de contenido (dashboard)
        content_frame = tk.Frame(self, bg="white")
        content_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        content_frame.pack(fill="x")

        # Tarjetas resumen
        resumen_frame = tk.Frame(content_frame, bg="white")
        resumen_frame.pack(fill="x", pady=10)

        self._crear_tarjeta(resumen_frame, "Ingresos", self.servicios["analytics"].total_por_tipo(self.usuario.id)["ingreso"])
        self._crear_tarjeta(resumen_frame, "Gastos", self.servicios["analytics"].total_por_tipo(self.usuario.id)["gasto"])
        self._crear_tarjeta(resumen_frame, "Deuda pendiente", self.servicios["deuda"].total_adeudado(self.usuario.id))
        self._crear_tarjeta(resumen_frame," Presupuesto usado", self.servicios["analytics"].total_por_tipo(self.usuario.id)["gasto"] )

    def _crear_tarjeta(self, parent, titulo, valor):
        frame = tk.Frame(parent, bg="#F0F0F0", bd=1, relief="solid")
        frame.pack(side="left", expand=True, fill="x", padx=5)

        lbl_titulo = tk.Label(frame, text=titulo, font=("Helvetica", 12, "bold"), bg="#F0F0F0")
        lbl_titulo.pack(pady=(10, 0))

        lbl_valor = tk.Label(frame, text=f"Q {valor:.2f}", font=("Helvetica", 14), bg="#F0F0F0", fg="#333")
        lbl_valor.pack(pady=(5, 10))

