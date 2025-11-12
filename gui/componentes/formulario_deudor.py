# app/gui/componentes/formulario_deudor.py

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from dominio.entidades.deudor import Deudor
from dominio.objetos_valor.estado_deuda import EstadoDeuda

class FormularioDeudor(tk.Toplevel):
    def __init__(self, master, usuario, servicio_deudor, on_guardar):
        super().__init__(master)
        self.usuario = usuario
        self.servicio_deudor = servicio_deudor
        self.on_guardar = on_guardar

        self.title("Registrar deudor")
        self.geometry("400x300")
        self.configure(bg="white")

        self.campos = {}

        self._agregar_campo("Nombre")
        self._agregar_campo("Monto")
        self._agregar_campo("Contacto")
        self._agregar_campo("Plazo inicio")
        self._agregar_campo("Plazo fin")

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
            nombre = self.campos["Nombre"].get().strip()
            finicio = self.campos["Plazo inicio"].get().strip()
            ffin = self.campos["Plazo fin"].get().strip()
            monto = float(self.campos["Monto"].get().strip())
            contacto = self.campos["Contacto"].get().strip()
        except Exception:
            messagebox.showerror("Error", "Verifica que los campos estén completos y correctos.")
            return

        deudor = Deudor(
            id=None,
            id_usuario=self.usuario.id,
            nombre=nombre,
            cantidad=monto,
            estado=EstadoDeuda("pendiente"),
            contacto=contacto,
            plazo_fin=datetime.fromisoformat(ffin).isoformat(),
            plazo_inicio=datetime.fromisoformat(finicio).isoformat(),
        )

        self.servicio_deudor.crear(deudor)
        self.on_guardar()
        self.destroy()
