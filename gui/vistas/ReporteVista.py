import tkinter as tk
#from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import datetime, timedelta

from logica.analitica_logica import AnalyticsService
from gestores.transacciones_gestor import TransactionsRepo
from gestores.presupuestos_gestor import PresupuestosRepo

class DashboardView(tk.Frame):
    def __init__(self, master, usuario):
        super().__init__(master)
        self.usuario = usuario
        self.analytics = AnalyticsService(TransactionsRepo(), PresupuestosRepo())
        self.configure(bg="white")
        self.pack(fill="both", expand=True)

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

        hoy = datetime.now().date()
        inicio = hoy - timedelta(days=30)
        id_usuario = self.usuario.id

        # Datos
        ingresos = self._suma(self.analytics.evolucion_por_tipo(id_usuario, "ingreso"), inicio, hoy)
        gastos = self._suma(self.analytics.evolucion_por_tipo(id_usuario, "gasto"), inicio, hoy)
        balance = ingresos - gastos

        deudas = self._suma(self.analytics.evolucion_deudas(id_usuario), inicio, hoy)
        deudores = self._suma(self.analytics.evolucion_deudores(id_usuario), inicio, hoy)

        presupuestos = self.analytics.evolucion_presupuestos(id_usuario)
        asignado = sum(v["asignado"] for f, v in presupuestos.items() if inicio.isoformat() <= f <= hoy.isoformat())
        usado = sum(v["usado"] for f, v in presupuestos.items() if inicio.isoformat() <= f <= hoy.isoformat())

        # Tarjetas
        fila1 = tk.Frame(self, bg="white")
        fila1.pack(pady=10)
        self._tarjeta(fila1, "Ingresos", ingresos)
        self._tarjeta(fila1, "Gastos", gastos)
        self._tarjeta(fila1, "Balance", balance)

        fila2 = tk.Frame(self, bg="white")
        fila2.pack(pady=10)
        self._tarjeta(fila2, "Deudas", deudas)
        self._tarjeta(fila2, "Deudores", deudores)
        self._tarjeta(fila2, "Presupuesto usado", f"{usado:.2f} / {asignado:.2f}")

    def _tarjeta(self, master, titulo, valor):
        frame = tk.Frame(master, bg="#F0F0F0", bd=1, relief="solid", width=180, height=100)
        frame.pack(side="left", padx=10)
        frame.pack_propagate(False)

        tk.Label(frame, text=titulo, font=("Arial", 12, "bold"), bg="#F0F0F0").pack(pady=5)
        tk.Label(frame, text=f"Q {valor:.2f}" if isinstance(valor, (int, float)) else valor,
                 font=("Arial", 14), bg="#F0F0F0").pack()

    def _suma(self, datos: dict[str, float], inicio, fin) -> float:
        return sum(v for f, v in datos.items() if inicio.isoformat() <= f <= fin.isoformat())

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
