import tkinter as tk
from gui.componentes.encabezado_botones import EncabezadoBotones
from gui.componentes.tabla_registros import TablaRegistros
from gui.componentes.formulario_deudor import FormularioDeudor

from logica.deudor_logica import DeudorService
from gestores.deudores_gestor import DeudoresRepo

from logica.exportar_excel import exportar_excel

class DeudoresView(tk.Frame):
    def __init__(self, master, usuario):
        super().__init__(master)
        self.usuario = usuario
        self.tx_service = DeudorService(DeudoresRepo())

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
        columnas = ["Categoria", "Fecha de Inicio", "Fecha de Vencimiento", "Monto"]
        self.tabla = TablaRegistros(self, columnas)
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Cargar datos
        self._cargar_transacciones()

    def _cargar_transacciones(self):
        self.tabla.limpiar()
        transacciones = self.tx_service.listar_por_usuario(self.usuario.id)
        for tx in transacciones:
            self.tabla.agregar_fila([
                tx.nombre,
                tx.contacto,
                f"Q {tx.cantidad:.2f}",
                tx.plazo_inicio[:10],
                tx.plazo_fin[:10],
                tx.estado
            ])

    def _abrir_formulario(self):
        FormularioDeudor(
            self,
            usuario=self.usuario,
            servicio_deudor = self.tx_service,
            on_guardar=self._cargar_transacciones
        )

    def _exportar_pdf(self):
        print("Exportar a PDF (pendiente de implementación)")

    def _exportar_excel(self):
        exportar_excel(self.tabla.tree, "deudores.xlsx")