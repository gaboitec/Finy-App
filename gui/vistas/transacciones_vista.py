import tkinter as tk
from tkinter import ttk
from gui.componentes.encabezado_botones import EncabezadoBotones
from gui.componentes.tabla_registros import TablaRegistros
from gui.componentes.formulario_transaccion import FormularioTransaccion

from logica.transaccion_logica import TransaccionService
from gestores.transacciones_gestor import TransactionsRepo

class TransaccionesView(tk.Frame):
    def __init__(self, master, usuario, servicios):
        super().__init__(master)
        self.usuario = usuario
        self.servicios = servicios
        self.tx_service = TransaccionService(TransactionsRepo())
        self.configure(bg="white")
        self.pack(fill="both", expand=True)

        self._construir_interfaz()

    def _construir_interfaz(self):
        # Encabezado con botones
        encabezado = EncabezadoBotones(self, on_nuevo=self._abrir_formulario)
        encabezado.pack(fill="x", pady=10)

        # Tabla de registros
        columnas = ["Fecha", "Tipo", "Categoría", "Monto", "Descripción"]
        self.tabla = TablaRegistros(self, columnas)
        self.tabla.pack(fill="both", expand=True)

        # Cargar datos
        self._cargar_transacciones()

    def _cargar_transacciones(self):
        transacciones = self.servicios["analitycs"].obtener_por_usuario(self.usuario.id)
        for tx in transacciones:
            self.tabla.agregar_fila([
                tx.fecha[:10],
                tx.tipo.value,
                tx.categoria.nombre,
                f"Q {tx.cantidad:.2f}",
                tx.descripcion
            ])

    def _abrir_formulario(self):
        FormularioTransaccion(self, self.usuario, self.servicios["categorias"], on_guardar=self._cargar_transacciones)