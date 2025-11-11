import tkinter as tk
#from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime

class DashboardView(tk.Frame):
    def __init__(self, master, usuario, servicios):
        super().__init__(master, bg="white")
        self.usuario = usuario
        self.analytics = servicios["analytics"]
        self._construir_interfaz()

    def _construir_interfaz(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Gráfico circular: porcentaje de gastos por categoría
        pie_frame = tk.Frame(self, bg="white")
        pie_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self._crear_grafico_pie(pie_frame)

        # Gráfico de línea: evolución diaria de ingresos
        line_frame = tk.Frame(self, bg="white")
        line_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self._crear_grafico_linea(line_frame)

    def _crear_grafico_pie(self, frame):
        data = self.analytics.porcentaje_por_categoria(self.usuario.id, "gasto")
        categorias = list(data.keys())
        valores = list(data.values())

        fig, ax = plt.subplots(figsize=(4, 4))
        ax.pie(valores, labels=categorias, autopct="%1.1f%%", startangle=90)
        ax.set_title("Distribución de Gastos por Categoría (último mes)")
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def _crear_grafico_linea(self, frame):
        data = self.analytics.evolucion_por_tipo(self.usuario.id, "ingreso")
        fechas = [datetime.strptime(k, "%Y-%m-%d") for k in data.keys()]
        valores = list(data.values())

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(fechas, valores, marker="o", color="green")
        ax.set_title("Evolución Diaria de Ingresos (último mes)")
        ax.set_xlabel("Fecha")
        ax.set_ylabel("Cantidad (Q)")
        fig.autofmt_xdate()
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
