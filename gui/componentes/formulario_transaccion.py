from gui.componentes.formulario_base import FormularioBase
from gui.componentes.formulario_categoria import FormularioCategoria
import tkinter as tk

class FormularioTransaccion(FormularioBase):
    def __init__(self, master, usuario, servicio_categoria, on_guardar):
        super().__init__(master, "Nueva transacción")
        self.usuario = usuario
        self.servicio_categoria = servicio_categoria
        self.on_guardar = on_guardar

        categorias = [c.nombre for c in self.servicio_categoria.obtener_todas()]
        self.agregar_campo("Fecha")
        self.agregar_campo("Tipo")  # ingreso/gasto
        self.agregar_campo("Categoría", tipo="combo", opciones=categorias)
        self.agregar_campo("Monto")
        self.agregar_campo("Descripción")

        btn_guardar = tk.Button(self, text="Guardar", command=self._guardar)
        btn_guardar.pack(pady=10)

        btn_nueva_cat = tk.Button(self, text="+ Nueva categoría", command=self._nueva_categoria)
        btn_nueva_cat.pack()

    def _guardar(self):
        datos = self.obtener_valores()
        # Aquí puedes validar y guardar usando el servicio
        self.on_guardar()
        self.destroy()

    def _nueva_categoria(self):
        FormularioCategoria(self, self.servicio_categoria, on_guardar=self._recargar_categorias)

    def _recargar_categorias(self):
        # Recargar opciones del combo
        nuevas = [c.nombre for c in self.servicio_categoria.obtener_todas()]
        self.campos["Categoría"].set(nuevas[0])