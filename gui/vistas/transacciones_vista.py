import tkinter as tk
from gui.componentes.encabezado_botones import EncabezadoBotones
from gui.componentes.tabla_registros import TablaRegistros
from gui.componentes.formulario_transaccion import FormularioTransaccion

from logica.transaccion_logica import TransaccionService
from gestores.transacciones_gestor import TransactionsRepo
from logica.categoria_logica import CategoriaService
from gestores.categorias_gestor import CategoriasRepo

class TransaccionesView(tk.Frame):
    def __init__(self, master, usuario):
        super().__init__(master)
        self.usuario = usuario
        self.tx_service = TransaccionService(TransactionsRepo())
        self.cat_service = CategoriaService(CategoriasRepo())

        self.configure(bg="white")
        self.pack(fill="both", expand=True)

        self._construir_interfaz()

    def _construir_interfaz(self):
        # Encabezado con botones
        encabezado = EncabezadoBotones(
            self,
            on_nuevo=self._abrir_formulario,
            on_exportar_pdf=self._exportar_pdf,
            on_exportar_excel=self._exportar_excel
        )
        encabezado.pack(fill="x", pady=10, padx=10)

        # Tabla de registros
        columnas = ["Fecha", "Tipo", "Categoría", "Monto", "Descripción"]
        self.tabla = TablaRegistros(self, columnas)
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Cargar datos
        self._cargar_transacciones()

    def _cargar_transacciones(self):
        self.tabla.limpiar()
        transacciones = self.tx_service.obtener_por_usuario(self.usuario.id)
        for tx in transacciones:
            self.tabla.agregar_fila([
                tx.fecha[:10],
                tx.tipo.value.capitalize(),
                tx.categoria,
                f"Q {tx.cantidad:.2f}",
                tx.descripcion or ""
            ])

    def _abrir_formulario(self):
        FormularioTransaccion(
            self,
            usuario=self.usuario,
            servicio_categoria=self.cat_service,
            servicio_tx = self.tx_service,
            on_guardar=self._cargar_transacciones
        )

    def _exportar_pdf(self):
        print("Exportar a PDF (pendiente de implementación)")

    def _exportar_excel(self):
        print("Exportar a Excel (pendiente de implementación)")