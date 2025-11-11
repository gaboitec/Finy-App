from gui.componentes.formulario_base import FormularioBase
from gui.componentes.formulario_categoria import FormularioCategoria

import tkinter as tk

class FormularioTransaccion(FormularioBase):
    def __init__(self, master, usuario, servicio_categoria, servicio_tx, on_guardar):
        super().__init__(master, "Nueva transacción")
        self.usuario = usuario
        self.servicio_categoria = servicio_categoria
        self.servicio_tx = servicio_tx
        self.on_guardar = on_guardar

        categorias = [c.nombre for c in self.servicio_categoria.listar_por_usuario(self.usuario.id)]
        self.agregar_campo("Tipo", tipo="combo", opciones=["ingreso","gasto"])
        self.agregar_campo("Categoria", tipo="combo", opciones=categorias)
        btn_nueva_cat = tk.Button(self, text="+ Nueva categoría", command=self._nueva_categoria)
        btn_nueva_cat.pack(pady=10, padx=5)
        self.agregar_campo("Monto")
        self.agregar_campo("Metodo",tipo="combo", opciones=["efectivo", "tarjeta","transferencia","otro"])
        self.agregar_campo("Descripcion")

        btn_guardar = tk.Button(self, text="Guardar", command=self._guardar)
        btn_guardar.pack(pady=10)

    def _guardar(self):
        datos = self.obtener_valores()
        self.servicio_tx.agregar_transaccion(self.usuario.id, datos["Categoria"], datos["Tipo"], datos["Monto"], datos["Descripcion"], datos["Metodo"])
        self.on_guardar()
        self.destroy()

    def _nueva_categoria(self):
        FormularioCategoria(self, self.servicio_categoria, self.usuario.id, on_guardar=self._recargar_categorias)

    def _recargar_categorias(self):
        # Recargar opciones del combo
        nuevas = [c.nombre for c in self.servicio_categoria.listar_por_usuario(self.usuario.id)]
        self.campos["Categoria"].set(nuevas[0])