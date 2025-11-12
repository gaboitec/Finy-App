import tkinter as tk
from gui.componentes.encabezado_botones import EncabezadoBotones
from gui.componentes.tabla_registros import TablaRegistros
from gui.componentes.formulario_deuda import FormularioDeuda

from logica.deuda_logica import DeudaService
from gestores.deudas_gestor import DeudasRepo
from logica.categoria_logica import CategoriaService
from gestores.categorias_gestor import CategoriasRepo

class DeudasView(tk.Frame):
    def __init__(self, master, usuario):
        super().__init__(master)
        self.usuario = usuario
        self.tx_service = DeudaService(DeudasRepo())
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
        columnas = ["Plazo de Inicio", "Plazo de Vencimiento", "Fecha de Pago", "Monto", "Interés", "Descripción"]
        self.tabla = TablaRegistros(self, columnas)
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Cargar datos
        self._cargar_transacciones()

    def _cargar_transacciones(self):
        self.tabla.limpiar()
        transacciones = self.tx_service.listar_por_usuario(self.usuario.id)
        for tx in transacciones:
            self.tabla.agregar_fila([
                tx.plazo_inicio[:10],
                tx.plazo_fin[:10],
                tx.fecha_pago[:10],
                tx.interes,
                tx.descripcion or ""
                f"Q {tx.cantidad:.2f}",
            ])

    def _abrir_formulario(self):
        FormularioDeuda(
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