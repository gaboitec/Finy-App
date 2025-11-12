# app/gui/componentes/formulario_deuda.py

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from dominio.entidades.deuda import Deuda
from dominio.objetos_valor.estado_deuda import EstadoDeuda

class FormularioDeuda(tk.Toplevel):
    def __init__(self, master, usuario, servicio_deuda, on_guardar):
        super().__init__(master)
        self.usuario = usuario
        self.servicio_deuda = servicio_deuda
        self.on_guardar = on_guardar

        self.title("Registrar deuda")
        self.geometry("400x300")
        self.configure(bg="white")

        self.campos = {}

        self._agregar_campo("Descripción")
        self._agregar_campo("Monto")
        self._agregar_campo("Fecha de pago")
        self._agregar_campo("Plazo de inicio")
        self._agregar_campo("Plazo de vencimiento")
        self._agregar_campo("Interes")

        btn_guardar = tk.Button(self, text="Guardar", command=self._guardar)
        btn_guardar.pack(pady=10)

    def _agregar_campo(self, etiqueta):
        frame = tk.Frame(self, bg="white")
        frame.pack(fill="x", pady=5, padx=10)
        tk.Label(frame, text=etiqueta + ":", bg="white").pack(anchor="w")
        entrada = tk.Entry(frame)
        entrada.pack(fill="x")
        self.campos[etiqueta] = entrada

    def _guardar(self):
        try:
            descripcion = self.campos["Descripción"].get().strip()
            monto = float(self.campos["Monto"].get().strip())
            fecha_limite = datetime.fromisoformat(self.campos["Fecha de pago"].get().strip()).isoformat()
            fecha_i = datetime.fromisoformat(self.campos["Fecha de inicio"].get().strip()).isoformat()
            fecha_f = datetime.fromisoformat(self.campos["Fecha de vencimiento"].get().strip()).isoformat()
            interes = float(self.campos["Interes"].get().strip())
        except Exception:
            messagebox.showerror("Error", "Verifica que los campos estén completos y correctos.")
            return

        deuda = Deuda(
            id=None,
            id_usuario=self.usuario.id,
            cantidad=monto,
            descripcion=descripcion,
            fecha_pago=fecha_limite,
            estado=EstadoDeuda("pendiente"),
            plazo_inicio=fecha_i,
            plazo_fin=fecha_f,
            interes=interes
        )

        self.servicio_deuda.crear(deuda)
        self.on_guardar()
        self.destroy()
